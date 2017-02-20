# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: Constraint propagation uses a method of checking a rule(constraint), which forces a solution in 
    all dependent boxes.  The constraint says that if there is a single pair of numbers in one unit,
    then it forces the removal of those numbers from other boxes in the same unit. To implement this, 
    it is necessary to find all 2 digit boxes, and see if 2 exist in the same unit.  if this constraint
    is found to be true, you check all other boxes in the unit and remove the single digits, found in 
    the naked-twins, from those numbers.  This can be repeated on multiple reduced versions of the
    puzzle, as further reductions are applied.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The solution to a diagonal Sudoku puzzle is similar to a regular Sudoku puzzle, with the additional
    constraint of 2 diagonal units, an identity type matrix (diagonals), and column swapped 
    type matrix(opposite diagonals).  When solving a diagonal puzzle, the methods used in a normal Sudoku
    are then applied with this additional set of constraints.  These constraints include Eliminate, 
    Only-Choice, Naked-Twins, and a search strategy of Depth First Search. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.