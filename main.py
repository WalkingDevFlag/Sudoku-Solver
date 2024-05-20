import img_grab
import cv2
import numpy as np
from PIL import ImageGrab

def main():
    x1, y1 = 293, 299
    x2, y2 = 826, 831
    gray = img_grab.screen_grab(x1, y1, x2, y2)
    
    # Display the grayscale image
    cv2.imshow('Grayscale Screen Capture', gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
