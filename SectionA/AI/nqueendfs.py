# Recursive solution for N-Queens problem in Python

from math import *
import sys


def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, n):
    if col >= n:
        return True

    for i in range(n):

        if isSafe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            if solve_nqueens(board, col + 1, n):
                return True

            board[i][col] = 0

    return False


def main():
    n = int(input())
    # n = 3
    board = [[0] * n for i in range(n)]
    if not solve_nqueens(board, 0, n):
        print("Solution does not exist")
        return False
    print()
    printSolution(board, n)
    return True


if __name__ == "__main__":
    main()