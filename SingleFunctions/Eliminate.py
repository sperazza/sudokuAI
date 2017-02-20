from GridValuesExpansionSoln import *
from utilsDiagonal import *
from GridValueSoln import *

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    for key, value in values.items():
        if len(value) == 1:
            for peer in peers[key]:
                keyString = values[peer]
                newkeyString = keyString.replace(value, '')
                values[peer] = newkeyString
    return values

    # retDict = values.copy()
    # for key, value in retDict.items():
    #     retDict[key] = value
    #     if len(value) == 1:
    #         for peer in peers[key]:
    #             keyString = retDict[peer]
    #             newkeyString = keyString.replace(value, '')
    #             retDict[peer] = newkeyString
    # return retDict


if __name__ == "__main__":
    grid_dic = grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    display(grid_dic)
    grid_dic = grid_values_expansion('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')
    display(grid_dic)
    elimDic = eliminate(grid_dic)
    print("\n")
    display(elimDic)

    elimDic = eliminate(grid_dic)
    print("\n")
    display(elimDic)

    elimDic = eliminate(grid_dic)
    print("\n")
    display(elimDic)

    elimDic = eliminate(grid_dic)
    print("\n")
    display(elimDic)

    elimDic = eliminate(grid_dic)
    print("\n")
    display(elimDic)



    for _ in range(8):
        elimDic = eliminate(grid_dic)
        grid_dic=elimDic.copy()

    print("\n")
    elimDic = eliminate(grid_dic)
    display(elimDic)

