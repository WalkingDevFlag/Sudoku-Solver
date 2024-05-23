# Sudoku Solver with CNN OCR (Under Development)

This Python script aims to solve Sudoku puzzles using image processing and a Convolutional Neural Network (CNN) based Optical Character Recognition (OCR) model. Please note that this project is still under development and may not be perfect.

## Features

- Captures a Sudoku grid from a screenshot
- Utilizes a CNN-based OCR model to extract numbers from the grid
- Solves the Sudoku puzzle using a backtracking algorithm
- Displays the solved Sudoku grid

## Prerequisites

- Python 3.x
- OpenCV (`cv2`)
- Numpy (`numpy`)
- Pillow (`PIL`)
- TensorFlow (`tensorflow`)
- Keras (`keras`)

## Installation

1. Install Python 3.x from the official website: https://www.python.org/downloads/
2. Install the required Python packages using pip:
3. Download the `ocr.h5` file containing the trained OCR model.

## Usage

1. Run the `main.py` script.
2. The script will capture a Sudoku grid from the screen based on the specified coordinates.
3. The captured image will be processed using the CNN OCR model to extract numbers.
4. The Sudoku puzzle will be solved using the backtracking algorithm.
5. The solved Sudoku grid will be displayed.

## Files

- `main.py`: The main script that captures the Sudoku grid, processes it with the CNN OCR model, and solves the puzzle.
- `img_grab.py`: Contains functions for capturing and preprocessing the Sudoku grid image.
- `ocr.py`: Includes functions for loading the OCR model, preprocessing images, and performing OCR with the CNN model.
- `backtracking.py`: Implements the backtracking algorithm to solve the Sudoku puzzle.
- `OCR.ipynb`: Jupyter notebook for training the CNN OCR model.

## CNN OCR Model Training

The `OCR.ipynb` notebook is used to train the Convolutional Neural Network (CNN) based Optical Character Recognition (OCR) model. The model is trained on the MNIST dataset, which contains handwritten digits.

The notebook includes the following steps:

1. Importing the necessary packages for building and training the CNN model.
2. Defining a function `build_model` to construct the CNN architecture.
3. Loading the MNIST dataset and preprocessing the data.
4. Compiling the CNN model with the Adam optimizer and categorical cross-entropy loss.
5. Training the model using the `fit` function and evaluating its performance on the test set.
6. Displaying the classification report to assess the model's accuracy.
7. Serializing the trained model to disk as `ocr.h5`.

The CNN model architecture consists of the following layers:

1. **Input layer**: The input shape is set to (28, 28, 1), representing the grayscale images from the MNIST dataset.

2. **First set of CONV => RELU => POOL layers**:
   - Convolutional layer with 32 filters of size (5, 5) and same padding.
   - ReLU activation function.
   - Max pooling layer with pool size (2, 2).

3. **Second set of CONV => RELU => POOL layers**:
   - Convolutional layer with 32 filters of size (3, 3) and same padding.
   - ReLU activation function.
   - Max pooling layer with pool size (2, 2).

4. **First set of FC => RELU layers**:
   - Flatten layer to convert the feature maps into a 1D vector.
   - Fully connected layer with 64 units.
   - ReLU activation function.
   - Dropout layer with a rate of 0.5 for regularization.

5. **Second set of FC => RELU layers**:
   - Fully connected layer with 64 units.
   - ReLU activation function.
   - Dropout layer with a rate of 0.5 for regularization.

6. **Output layer**:
   - Fully connected layer with 10 units (one for each digit class).
   - Softmax activation function to obtain class probabilities.

The trained model is saved as `ocr.h5` and can be used for performing OCR on the Sudoku grid images in the main project.

## Note

This project is still in development, and the OCR model may not be perfect. There is no specific license associated with this project.

Feel free to contribute, provide feedback, or suggest improvements to enhance the functionality and accuracy of the Sudoku solver with CNN OCR.

Remember to handle the trained OCR model with care and ensure proper attribution if necessary.

Enjoy exploring and developing this Sudoku solver project with CNN OCR!
