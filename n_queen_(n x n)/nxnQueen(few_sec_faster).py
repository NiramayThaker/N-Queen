import copy
import random


def board_size_input():
    while True:
        try:
            chess_board_size = int(input('Enter the size of chessboard (chess_board_size) -> '))
            if chess_board_size <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            return chess_board_size
        except ValueError:
            print("Invalid value ..! Enter again")


def is_queen_safe(board, row, col, n):
    for j in range(col):
        if board[row][j] == "Q":
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i = i - 1
        j = j - 1

    x, y = row, col
    while x < n and y >= 0:
        if board[x][y] == "Q":
            return False
        x = x + 1
        y = y - 1

    return True


def create_board(n):
    board = ["x"] * n
    for i in range(n):
        board[i] = ["x"] * n
    return board


def output(solutions, n):
    random_solution = random.randint(0, len(solutions) - 1)
    for row in solutions[random_solution]:
        print(" ".join(row))


def copy_save_solution(board):
    global solutions
    if len(solutions) < 1:
        saved_board = copy.deepcopy(board)
        solutions.append(saved_board)


def solve(board, col, n):
    if col >= n:
        return

    for i in range(n):
        if is_queen_safe(board, i, col, n):
            board[i][col] = "Q"
            if col == n - 1:
                copy_save_solution(board)
                board[i][col] = "x"
                return
            solve(board, col + 1, n)
            board[i][col] = "x"


n = board_size_input()
board = create_board(n)
solutions = []
solve(board, 0, n)
output(solutions, n)
