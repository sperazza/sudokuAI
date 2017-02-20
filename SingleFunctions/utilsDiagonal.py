"""
We'll start by writing a helper function, cross(a, b), which, given two
strings — a and b — will return the list formed by all the possible concatenations
 of a letter S in string A with a letter T in string B.

So cross('abc', 'def') will return ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].
def cross(a, b):
      return [s+t for s in a for t in b]
"""

rows = 'ABCDEFGHI'
cols = '123456789'

diagonal_sudoku = True


def cross(a, b):
    return [s + t for s in a for t in b]


def diagonal_cross(a, b):
    return [s + t for s in a for t in b if a.index(s) == b.index(t) or len(a) - 1 - a.index(s) == b.index(t)]


boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
diagonal_units = [diagonal_cross(rows, cols)]

unitlist = row_units + column_units + square_units
if diagonal_sudoku:
    unitlist += diagonal_units

units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in boxes)


def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

# unitlist = row_units + column_units + square_units + [[x] for x in diagonal_units[0] if diagonal_sudoku]




# print(peers['A9'])
# print("ru=",row_units)
# print("du=",diagonal_units)
# print(diagonal_cross(rows, cols))
# print(units)
# print(len(units))
# print(unitlist)
# print(len(unitlist))
