# N is global variable stands for board size
global N
N = 4


# It will display solution
def display_solution(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# checking is queen safe from attack
# We have to check it for left side of board as first queen will be on right already
def is_queen_safe(board, row, col):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve(board, col):
    # if all queens are placed then return true
    if col >= N:
        return True

    # placing queens
    for i in range(N):

        if is_queen_safe(board, i, col):
            board[i][col] = 1

            # recur to place rest of the queens
            if solve(board, col + 1) == True:
                return True
            # If placing queen at board[i][col] doesn't give solution
            # start backtracking
            board[i][col] = 0

    # Return false if queen can't we placed at any place
    return False


# solve() is having backtracking it will return true if queen is placed and false if not
# Where you can see 1 is the place where queen is placed

def to_run():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

    if solve(board, 0) == False:
        print("Solution does not exist")
        return False

    display_solution(board)
    return True


to_run()
