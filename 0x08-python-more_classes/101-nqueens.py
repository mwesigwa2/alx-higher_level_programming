#!/usr/bin/python3
"""N queens puzzle"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the current row or diagonals
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def nqueens_util(board, row, N):
    if row == N:
        print(' '.join(str(col + 1) for col in board))
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            nqueens_util(board, row + 1, N)


def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    nqueens_util(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
