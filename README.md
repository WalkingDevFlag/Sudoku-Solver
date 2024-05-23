# Sudoku Solver

This is a Python script that solves Sudoku puzzles using image processing and a backtracking algorithm.

## Features

- Captures a Sudoku grid from a screenshot
- Uses Optical Character Recognition (OCR) to extract numbers from the grid
- Solves the Sudoku puzzle using a backtracking algorithm
- Displays the solved Sudoku grid

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- Pillow (`PIL`)
- Pytesseract (`pytesseract`)

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the required Python packages using pip:
3. Download and install Tesseract OCR Engine from the official website: https://github.com/tesseract-ocr/tesseract/wiki/Downloads
4. Update the `pytesseract.pytesseract.tesseract_cmd` variable in the `ocr.py` file with the path to your Tesseract executable.

## Usage

1. Run the `main.py` script.
2. The script will capture a Sudoku grid from the screen based on the specified coordinates (`x1`, `y1`, `x2`, `y2`).
3. The captured image will be processed using OCR to extract the numbers from the grid.
4. The Sudoku puzzle will be solved using the backtracking algorithm.
5. The solved Sudoku grid will be displayed.

## Files

- `main.py`: The main script that captures the Sudoku grid, processes it, and solves the puzzle.
- `img_grab.py`: Contains functions for capturing and preprocessing the Sudoku grid image.
- `ocr.py`: Includes functions for dividing the Sudoku grid into cells, extracting numbers from the cells using OCR, and processing the Sudoku grid.
- `backtracking.py`: Implements the backtracking algorithm to solve the Sudoku puzzle.

## Contributing

If you find any issues or have suggestions for improvements, feel free to create a new issue or submit a pull request on the project's GitHub repository.

## License

This project is not licensed
