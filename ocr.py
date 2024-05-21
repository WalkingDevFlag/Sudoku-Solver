import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def divide(grid_size=532, num_cells=9):
    cell_size = grid_size // num_cells
    cells = []
    
    for row in range(num_cells):
        for col in range(num_cells):
            x1 = col * cell_size
            y1 = row * cell_size
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            cells.append((x1, y1, x2, y2))
    
    return cells

def capture_roi(x1, y1, x2, y2, img):
    roi = img[y1:y2, x1:x2]
    return roi

def extract_number_from_image(roi):
    config = '--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789'
    number = pytesseract.image_to_string(roi, config=config)
    number = ''.join(filter(str.isdigit, number))
    if number:
        return int(number)
    else:
        return 0

def process(cells, img):
    sudoku_array = [[0 for _ in range(9)] for _ in range(9)]
    
    for idx, cell in enumerate(cells):
        x1, y1, x2, y2 = cell
        roi = capture_roi(x1, y1, x2, y2, img)
        
        number = extract_number_from_image(roi)
        
        row = idx // 9
        col = idx % 9
        
        if number:
            sudoku_array[row][col] = number
            print(f"Cell {row+1}-{col+1}: Number identified - {number}")
        else:
            sudoku_array[row][col] = 0
            print(f"Cell {row+1}-{col+1}: No number identified - 0")
        
        # Display the ROI for visual verification
        #cv2.imshow('ROI', roi)
        #cv2.waitKey(0)
    
    return sudoku_array
