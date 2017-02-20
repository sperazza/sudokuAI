
from collections import defaultdict

assignments = []


class SudokuDiagonalStructure(object):
    """
    Initialize structure elements for diagonal sudoku puzzle, this allows swapping between
    conventional and diagonal solutions
    """

    def __init__(self):
        self.rows = 'ABCDEFGHI'
        self.cols = '123456789'

        def cross(a, b):
            return [s + t for s in a for t in b]

        def diagonal_cross(a, b):
            return [s + t for s in a for t in b if a.index(s) == b.index(t)]

        def diagonal_cross2(a, b):
            return [s + t for s in a for t in b if len(a) - 1 - a.index(s) == b.index(t)]

        self.boxes = cross(self.rows, self.cols)
        self.row_units = [cross(r, self.cols) for r in self.rows]
        self.column_units = [cross(self.rows, c) for c in self.cols]
        self.square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
        self.diagonal_units1 = [diagonal_cross(self.rows, self.cols)]
        self.diagonal_units2 = [diagonal_cross2(self.rows, self.cols)]
        self.unitlist = self.diagonal_units1 + self.diagonal_units2 + self.row_units + self.column_units + self.square_units

        self.units = dict((s, [u for u in self.unitlist if s in u]) for s in self.boxes)
        self.peers = dict((s, set(sum(self.units[s], [])) - set([s])) for s in self.boxes)


def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    for unit in unitlist:
        naked_dict = defaultdict(list)
        construct_dic_of_naked_twins(naked_dict, unit, values)
        naked_list = {k: v for k, v in naked_dict.items() if len(v) == 2}
        remove_naked_from_peer_units(naked_list, unit, values)
    return values


def remove_naked_from_peer_units(naked_list, unit, values):
    for naked_digits, _ in naked_list.items():
        for peer in unit:
            for single_digit in naked_digits:
                if single_digit in values[peer] and naked_digits != values[peer]:
                    values[peer] = values[peer].replace(single_digit, '')
                    values = assign_value(values, peer, values[peer])


def construct_dic_of_naked_twins(naked_dict, unit, values):
    for idx, item in enumerate(unit):
        if len(values[item]) == 2:
            naked_dict[values[item]].append(idx)


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    grid_dic = {}
    letters = [letter for letter in grid]
    for idx, cell in enumerate(boxes):
        if letters[idx] == '.':
            grid_dic[cell] = '123456789'
            continue
        grid_dic[cell] = letters[idx]
    return grid_dic


def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF':
            print(line)
    return


def eliminate(values):
    solved_values_keys = [box for box in values.keys() if len(values[box]) == 1]
    for box_key in solved_values_keys:
        single_digit = values[box_key]
        for peer in peers[box_key]:
            if len(values[peer]) > 1:
                values[peer] = values[peer].replace(single_digit, '')
                assign_value(values, peer, values[peer])
    return values


def only_choice(values):
    for unit in unitlist:
        for box1 in unit:
            unit_set = set()
            one_box_set = {x for x in values[box1]}
            for box in unit:
                if box != box1:
                    unit_set |= set(values[box])
            final_set = one_box_set - unit_set
            if len(final_set) == 1:
                values[box1] = list(final_set)[0]
                assign_value(values, box1, values[box1])
    return values


def reduce_puzzle(values):
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values


def is_all_single_digits(values):
    for box in values.keys():
        if len(values[box]) > 1:
            return False
    return True


solved = False


def search(values):
    global solved
    values = reduce_puzzle(values)
    if values is False:
        return False
    if is_all_single_digits(values):
        return values
    sorted_values = list(dict(
        [(sorted_key, values[sorted_key]) for sorted_key in sorted(values, key=lambda k: len(values[k]), reverse=False)
         if len(values[sorted_key]) > 1]))
    for value in values[sorted_values[0]]:
        new_values = values.copy()
        new_values[sorted_values[0]] = value
        new_value_set = search(new_values)
        if new_value_set:
            return new_value_set


s = SudokuDiagonalStructure()
rows = s.rows
cols = s.cols
boxes = s.boxes
unitlist = s.unitlist
units = s.units
peers = s.peers


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    result = search(values)
    if result:
        print("Solved")
        return result
    print("not Solved")
    return values


if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments

        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')

