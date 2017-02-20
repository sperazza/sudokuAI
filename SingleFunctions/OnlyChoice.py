"""
If there is only one box in a unit which would allow a certain digit, then that box must be assigned that digit.

Time to code it! In the next quiz, finish the code for the function only_choice, which will take
as input a puzzle in dictionary form. The function will go through all the units,
 and if there is a unit with a digit that only fits in one possible box, it will assign that digit to that box.


"""

from Eliminate import *
from GridValueSoln import *


def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    for unit in unitlist:
        for box1 in unit:
            unitSet = set()
            oneBoxSet = {x for x in values[box1]}
            for box in unit:
                if box != box1:
                    unitSet = unitSet | set(values[box])
            finalSet = oneBoxSet - unitSet
            if (len(finalSet) == 1):
                values[box1] = list(finalSet)[0]

    # # TODO: Implement only choice strategy here
    return values


def only_choice_soln(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values


if __name__ == "__main__":
    print("\nStarting Soduku matrix:\n")
    display(grid_valuesOrig('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

    print("\n\nSoduku matrix Expansion:")
    grid_dic = grid_values_expansion(
        '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print("\n")
    display(grid_dic)

    grid_dic = eliminate(grid_dic)
    print("\n\nmatrix elimination:")
    display(grid_dic)

    grid_dic1 = grid_dic.copy()
    grid_dic2 = grid_dic.copy()

    print("\nGrid1 My Only Choice :")
    grid_dic1 = only_choice_mine(grid_dic1)
    print("\n")
    display(grid_dic1)

    print("\ngrid1 eliminate :")
    grid_dic1 = eliminate(grid_dic1)
    print("\n")
    display(grid_dic1)

    print("\ngrod1 My Only Choice :")
    grid_dic1 = only_choice_mine(grid_dic1)
    print("\n")
    display(grid_dic1)

    print("\ngrod1 eliminate :")
    grid_dic1 = eliminate(grid_dic1)
    print("\n")
    display(grid_dic1)

    print("\n\n================================================")
    print("\nSoln Only Choice :")
    grid_dic2 = only_choice(grid_dic2)
    print("\n")
    display(grid_dic2)

    print("\nSoln Only Choice :")
    grid_dic2 = only_choice(grid_dic2)
    print("\n")
    display(grid_dic2)

    print("\nSoln Only Choice :")
    grid_dic2 = eliminate(grid_dic2)
    print("\n")
    display(grid_dic2)

    print("\nSoln Only Choice :")
    grid_dic2 = only_choice(grid_dic2)
    print("\n")
    display(grid_dic2)

    print("\nStarting Soduku matrix:\n")
    display(grid_valuesOrig('.839216579..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))

    print("\n\nSoduku matrix Expansion:")
    grid_dic = grid_values_expansion(
        '.839216579..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    print("\n")
    display(grid_dic)

    grid_dic = eliminate(grid_dic)
    print("\n\nmatrix elimination:")
    display(grid_dic)

    grid_dic1 = grid_dic.copy()
    grid_dic2 = grid_dic.copy()

    print("\nGrid1 My Only Choice :")
    grid_dic1 = only_choice_mine(grid_dic1)
    print("\n")
    display(grid_dic1)


# seta={4,9}
# setb={2}
# setc={1,4,7}
# setd={3}
# sete={4,7}
# setf={5}
# setg={8}
# seth={7,9}
# seti={6}
#
# setu=set()
# setu=setu|seta
# setu=setu|setb
# setu=setu|setc
# setu=setu|setd
# setu=setu|sete
# setu=setu|setf
# setu=setu|setg
# setu=setu|seth
# setu=setu|seti
#
# print(setu)
# print(setc-setu)

# print("cell=", cell," peer=",peer)
#            print({x for x in values[peer]})
#   set+=set({x} for x in values[peer])
#   print(set)



# for unit in unitlist:
#     print(unit)
# for cell, vals in values.items():
# for unit in unitlist:
#     #print(unit)
#     cellpeers = [box for box in unit]
#     #print(cellpeers)
#     unitSet=set(cellpeers)
#     print(unitSet)
#     dplaces = [box for box in unit if '1' in values[box]]
#     #print(dplaces)
#     Cellset = set()
#
#     for peer in cellpeers:
#         tempset = {x for x in values[peer]}
#         Cellset=Cellset|tempset
#
#     myCellSet={x for x in values[box]}
#
#     CellResult=myCellSet-Cellset
#     if len(CellResult) == 1:
#         values[cell]=vals
#         #print("***1 found:",cell," ",vals)


# for cell, vals in values.items():
#     cellpeers = peers[cell]
#     Cellset = set()
#     for peer in cellpeers:
#         tempset = {x for x in values[peer]}
#         Cellset=Cellset|tempset
#     myCellSet={x for x in values[cell]}
#     CellResult=myCellSet-Cellset
#     if len(CellResult) == 1:
#         values[cell]=list(CellResult)[0]
#         #print("***1 found:",cell," ",vals)
# # TODO: Implement only choice strategy here
# return values

#     print("tempset=", tempset)
#     print("Cellset=", Cellset)
# print("cell=",cell)

# print("cell expand:", myCellSet)
