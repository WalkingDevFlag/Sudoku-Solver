import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# Load the Sudoku grid image
image = cv2.imread(r"sudoku_grid.jpg")

# Preprocess the image (convert to grayscale and apply thresholding)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Perform OCR on the preprocessed image
custom_config = r'--oem 3 --psm 6 outputbase digits'
text = pytesseract.image_to_string(thresh, config=custom_config)

# Convert the OCR result into a 2D array
sudoku_array = []
for line in text.split('\n'):
    row = []
    for char in line:
        if char.isdigit():
            row.append(int(char))
        else:
            row.append(0)
    sudoku_array.append(row)

# Print the 2D array representation of the Sudoku grid
for row in sudoku_array:
    print(row)
