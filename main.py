import img_grab
import cv2
import numpy as np
from PIL import ImageGrab
import ocr

def main():
    x1, y1 = 293, 299
    x2, y2 = 825, 831
    img = img_grab.screen_grab(x1, y1, x2, y2)
    
    # Display the captured image
    cv2.imshow('Captured Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cells = ocr.divide()
    sudoku_array = ocr.process(cells, img)
    
    print("Sudoku Grid:")
    for row in sudoku_array:
        print(row)

    print("\nCell Coordinates:")
    print(cells)

if __name__ == "__main__":
    main()
