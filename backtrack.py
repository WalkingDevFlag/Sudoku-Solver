'''
def is_valid(board, row, col, num):
    # TO  Check if the number is already present in the row
    for i in range(9):
        if board[row][i] == num:
            return False
    
    # Check if the number is already present in the column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already present in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # Puzzle solved
    
    row, col = empty_cell
    
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            if solve_sudoku(board):
                return True
            
            # Backtrack
            board[row][col] = 0
    
    return False  # No solution found

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None
    '''
