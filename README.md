# SudokuSolver

This repository contains an AI agent that can arguably solve any Sudoku puzzle in the world.

## Demo
This is how you would run the project in VS Code.

![](https://raw.githubusercontent.com/rafi007akhtar/SudokuSolver/master/solving.gif)

## Prerequisites
In order to try this out, your computer needs to have:

1. **Python 3 interpreter** (preferebly 3.4 or above).
2. An **text-editor** or an IDE. (I used _Visual Studio Code_.)
3. A **Terminal** / CMD (VS Code has one built-in).
3. (Optional) **Pygame**. Without Pygame, the program would still run, but you will only be able to see the solved board on the terminal, and _not_ the visualizations.

## Installation

1. Clone the repository.
2. Open a Terminal / CMD.
2. `cd` your way through the root of the repository.
4. Enter the following command.
    ```
        python solution.py
    ```
(If the above command didn't work, try replacing `python` with `python3`.)

To try it out with some other input, open `solution.py` and re-assign the varaible `diag_sudoku_grid` to your input board. The input is one, uninterrupted string with no spaces. The numbers are the numbers given on the board *row-wise*, and the periods represent an unfilled cell.
