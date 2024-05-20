import cv2
import numpy as np
from PIL import ImageGrab

def screen_grab(x1, y1, x2, y2):
    bbox = (x1, y1, x2, y2)
    screen = ImageGrab.grab(bbox=bbox)
    
    # Convert the image to a numpy array
    screen_np = np.array(screen)
    
    # Convert to grayscale
    gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)
    
    return gray
