import pyautogui as pg
import time
from pynput import mouse

grid = []

# Input Sudoku grid
while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    grid.append(ints)

    if len(grid) == 9:
        break
    print('Row ' + str(len(grid)) + ' Complete')

# Function to check if a number can be placed in a certain position
def possible(x, y, n):
    global grid
    for i in range(0, 9):
        if grid[i][x] == n and i != y:  # Check column
            return False

    for i in range(0, 9):
        if grid[y][i] == n and i != x:  # Check row
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Check 3x3 box
            if grid[Y][X] == n:
                return False
    return True

# Function to print the Sudoku grid using PyAutoGUI
def Print(grid):
    for y in range(9):
        for x in range(9):
            num = grid[y][x]
            if num != 0:
                pg.press(str(num))
            pg.hotkey('right')  # Move to the next column

        if y < 8:
            pg.hotkey('down')  # Move to the next row
            for _ in range(9):  # Move to the start of the next row
                pg.hotkey('left')

# Function to solve the Sudoku recursively
def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(x, y, n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    Print(grid)

# Listener function for mouse click
def on_click(x, y, button, pressed):
    if pressed:
        solve()
        return False  # Stop listener

# Wait for a mouse click to start typing
print('Waiting for a mouse click to start typing the Sudoku solution...')
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
