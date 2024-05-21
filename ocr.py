import cv2
import numpy as np
from tensorflow.keras.models import load_model

def load_ocr_model(model_path):
    model = load_model(model_path)
    return model

def preprocess_image(image):
    if image is None:
        raise ValueError("Image data is missing or invalid.")

    # Check the number of channels in the input image
    if len(image.shape) == 3 and image.shape[2] == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif len(image.shape) == 2:
        gray_image = image  # Image is already grayscale
    else:
        raise ValueError("Invalid number of channels in the input image.")

    resized_image = cv2.resize(gray_image, (28, 28))
    processed_image = resized_image.astype("float32") / 255.0
    processed_image = processed_image.reshape((1, 28, 28, 1))
    
    return processed_image

def perform_ocr(model, image):
    predictions = model.predict(image)
    return predictions

def capture_roi(x1, y1, x2, y2, img):
    roi = img[y1:y2, x1:x2]
    return roi

def extract_number_from_image_with_custom_ocr(roi, ocr_model):
    processed_roi = preprocess_image(roi)
    prediction = perform_ocr(ocr_model, processed_roi)
    number = np.argmax(prediction)
    return number

def process(img, ocr_model):
    cell_size = 532 // 9  # Define cell_size here
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]
    
    for row in range(9):
        for col in range(9):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            roi = capture_roi(x1, y1, x2, y2, img)

            number = extract_number_from_image_with_custom_ocr(roi, ocr_model)
            
            sudoku_array[row][col] = number
            print(f"Cell {row+1}-{col+1}: Number identified - {number}")
    
    return sudoku_array
