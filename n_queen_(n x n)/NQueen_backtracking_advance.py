import copy
import random


def board_size_input():
    # Taking user input for the size of the board
    while True:
        # Using try except to give multiple chance to user for input if entered wrong
        try:
            chess_board_size = int(input('Enter the size of chessboard (chess_board_size) -> '))
            if chess_board_size <= 3:
                print("Enter a value greater than or equal to 4")
                continue
            return chess_board_size
        except ValueError:
            print("Invalid value ..! Enter again")


# checking that is queen safe from attack
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

# if all of these upper condition in not true it means that queen is safe to place
    return True


def create_board(n):
    board = ["x"] * n
    for i in range(n):
        board[i] = ["x"] * n
    return board


def output(solutions, n):
    # Prints one of the solutions randomly
    random_solution = random.randint(0, len(solutions) - 1)
    for row in solutions[random_solution]:
        print(" ".join(row))


def copy_save_solution(board):
    # creating global variable which will save all the solutions
    global solutions
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
            solve(board, col + 1, n)  # Recursive[repetitive] call
            # Backtracking
            board[i][col] = "x"


# Saving user input of board size in n named variable
n = board_size_input()
# Binding ready board to board variable
board = create_board(n)
# Creating list to save all the solution
solutions = []
solve(board, 0, n)
print()
print("One random solution is :- \n")
output(solutions, n)
print()
# Randomly printing any of the one solution from all the possible ones
print(f"There are total ['{len(solutions)}'] way possible to solve it")
