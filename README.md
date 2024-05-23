# Sudoku Solver with OCR 

This Python script is designed to solve Sudoku puzzles using image processing and OCR (Optical Character Recognition). However, there is an issue highlighted where the OCR is able to recognize all the digits except that it is identifying one blank space as a digit.

## Features

- Captures a Sudoku grid from a screenshot
- Utilizes OCR to extract numbers from the grid
- Solves the Sudoku puzzle using a backtracking algorithm
- Displays the solved Sudoku grid

## Files

- `backtracking.py`: Contains functions for solving the Sudoku puzzle using backtracking.
- `img_grab.py`: Includes functions for capturing and preprocessing the Sudoku grid image.
- `ocr.py`: Implements OCR functions for extracting numbers from the grid.
- `main.py`: The main script that orchestrates the Sudoku solving process.

## Issue Highlighted

The OCR functionality in the script is able to recognize all the digits correctly, but it is incorrectly identifying one blank space as a digit. This issue may affect the accuracy of the Sudoku solving process.

## Usage

1. Run the `main.py` script to start the Sudoku solving process.
2. The script captures the Sudoku grid, processes it using OCR, and solves the puzzle.
3. The solved Sudoku grid will be displayed along with the identified numbers.

## Known Issue

The OCR component may incorrectly identify a blank space as a digit, impacting the accuracy of the Sudoku solving process. Further refinement of the OCR functionality may be required to address this issue.

Feel free to contribute, provide feedback, or suggest improvements to enhance the OCR accuracy and overall performance of the Sudoku solver.

Enjoy exploring and developing this Sudoku solver project with OCR functionality!
