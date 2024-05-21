import img_grab
import cv2
import numpy as np
from PIL import ImageGrab
import ocr
import backtracking

def main():
    x1, y1 = 293, 299
    x2, y2 = 825, 831
    img = img_grab.screen_grab(x1, y1, x2, y2)

    # Load the custom OCR model
    ocr_model = ocr.load_ocr_model('ocr.h5')

    sudoku_array = ocr.process(img, ocr_model)
    
    print("Sudoku Grid:")
    for row in sudoku_array:
        print(row)

    backtracking.solve(sudoku_array)
    backtracking.print_board(sudoku_array)

if __name__ == "__main__":
    main()
