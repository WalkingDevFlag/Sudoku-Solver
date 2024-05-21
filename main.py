import img_grab
import cv2
import numpy as np
from PIL import ImageGrab
import ocr
import backtracking
from backtracking import solve, valid, print_board, find_empty

def main():
    x1, y1 = 293, 299
    x2, y2 = 825, 831
    img = img_grab.screen_grab(x1, y1, x2, y2)
    #img = cv2.blur(img, (7, 6))

    
    # Display the captured image
    cv2.imshow('Captured Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

    cells = ocr.divide()
    sudoku_array = ocr.process(cells, img)
    
    print("Sudoku Grid:")
    for row in sudoku_array:
        print(row)

    backtracking.solve(sudoku_array)
    backtracking.print_board(sudoku_array)

if __name__ == "__main__":
    main()
