# SudokuSolver

This repository contains an AI agent that can arguably solve any Sudoku puzzle in the world.

## Demo
![](https://github.com/rafi007akhtar/SudokuSolver/objects/solving.gif)

### In order to try this out, your PC needs to have:

1. **Python 3 interpreter** (preferebly 3.6 or above).
2. An IDE that runs Python projects, like **PyCharm** or **Visual Studio**. I used Visual Studio 2017 (Community).
3. (Optional) **Pygame**. Without Pygame, the program would still run, but you won't see any visualizations, only results in the console.

Illustrative images can be found in the **screenshots** folder here: https://github.com/rafi007akhtar/SudokuSolver/tree/master/screenshots.

### To use this agent,

1. Clone the repository.
2. Open using Visual Studio (didn't try with PyCharm, so not sure if it'd work with it).
3. Right click on `solutions.py`, and click `Debug`

To try it out with some other input, open `source.py` and re-assign the varaible `diag_sudoku_grid` to your input board. The input is one, uninterrupted string with no spaces. The numbers are the numbers given on the board *row-wise*, and the periods represent an unfilled cell.
