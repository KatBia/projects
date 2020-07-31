import numpy as np


def getgrid():
    grid = []
    for x in range(9):
        x = input().split(',')
        grid.append(x)
    print(np.matrix(grid))
    return grid


def check(y, x, n):
    for i in range(0, 9):
        if int(grid[y][i]) == n:
            return False
    for i in range(0, 9):
        if int(grid[i][x]) == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3

    for i in range(0, 3):
        for j in range(0, 3):
            if int(grid[y0+i][x0+j]) == n:
                return False
    return True


def solve(grid):
    for y in range(9):
        for x in range(9):
            if int(grid[y][x]) == 0:
                for n in range(1, 10):
                    if check(y, x, n):
                        grid[y][x] = n
                        solve(grid)
                        grid[y][x] = 0
                return
    print(np.matrix(grid))


grid = getgrid()
solve(grid)
