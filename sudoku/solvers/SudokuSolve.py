import random
global solvedboard
solvedboard = []
def maker():
    board = [
        [5, 8, 6, 2, 9, 1, 7, 4, 3],
        [2, 9, 4, 3, 7, 8, 5, 6, 1],
        [3, 7, 1, 6, 5, 4, 2, 8, 9],
        [9, 3, 2, 4, 8, 6, 1, 5, 7],
        [8, 4, 7, 9, 1, 0, 3, 2, 6],
        [1, 6, 5, 7, 3, 2, 0, 9, 4],
        [4, 2, 3, 8, 6, 7, 9, 1, 5],
        [6, 5, 9, 1, 2, 3, 4, 7, 8],
        [7, 1, 8, 5, 4, 9, 6, 3, 2]
    ]
    for i in range(len(board)):
        for j in range(len(board)):
            if random.randrange(2, 5) == 4:
                board[i][j] = 0
    return board

def solve(boardm):
    #uses backtracking to sovle solution
    board = [0,0,0,0,0,0,0,0,0]  # this shenanigan is because it was changing the board itself and we don't want that.
    for i in range(len(boardm)):
        nb = boardm[i]
        board[i] = nb[:]
    find = find_empty(board)
    if find:
        row, col = find
    else:
        global solvedboard
        solvedboard = board
        return True
        # not empty so it is solved

    for i in range(1, 10):
        if valid(board, (row, col), i):
            board[row][col] = i

            if solve(board):
                # recursive call; if it fails later on it will return false and go back to this layer
                return True

            board[row][col] = 0
            # all the "solved" from the problem undo themselves.
    return False
def valid(board, pos, num):
    #row
    for i in range(0, len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #col
    for i in range(0, len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def checkBoard(board):
    for i in range (len(board)):
        for j in range(len(board[i])):
            val = board[i][j]
            if not valid(board,(i,j), val):
                return False
    return True


def find_empty(board):

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print(" | ", end= "")
            if j == 8:
                print(board[i][j], end="\n")
            else:
                print(str(board[i][j]) + " ", end="")


if __name__ == "__main__":

    board4 = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]
    board3 = [
        [5, 8, 6, 2, 9, 1, 7, 4, 3],
        [2, 9, 4, 3, 7, 8, 5, 6, 1],
        [3, 7, 1, 6, 5, 4, 2, 8, 9],
        [9, 3, 2, 4, 8, 6, 1, 5, 7],
        [8, 4, 7, 9, 1, 0, 3, 2, 6],
        [1, 6, 5, 7, 3, 2, 0, 9, 4],
        [4, 2, 3, 8, 6, 7, 9, 1, 5],
        [6, 5, 9, 1, 2, 3, 4, 7, 8],
        [7, 1, 8, 5, 4, 9, 6, 3, 2]
    ]
    board2 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # make scannable interface
    board6 = [
        [4, 0, 9, 0, 0, 2, 0, 7, 0],
        [3, 6, 0, 0, 8, 0, 0, 5, 0],
        [0, 0, 0, 5, 0, 0, 0, 0, 1],
        [7, 0, 0, 0, 9, 0, 1, 0, 0],
        [0, 2, 0, 4, 0, 8, 0, 9, 0],
        [0, 8, 5, 0, 3, 0, 0, 0, 6],
        [2, 0, 0, 0, 0, 6, 0, 0, 0],
        [0, 9, 0, 0, 1, 0, 0, 2, 7],
        [0, 4, 0, 3, 0, 0, 8, 0, 0]
    ]
    board = [
        [4, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 8, 0, 0, 2, 0, 6],
        [0, 0, 8, 0, 2, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 1, 9, 0, 0],
        [0, 1, 5, 3, 0, 9, 0, 4, 0],
        [0, 0, 6, 2, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 9, 2, 6, 0, 0],
        [6, 2, 3, 0, 0, 8, 0, 1, 0],
        [9, 0, 0, 0, 0, 0, 0, 2, 8]
    ]
    board10 = [[0, 0, 0, 0, 8, 0, 0, 0, 0], [9, 1, 7, 2, 0, 0, 0, 0, 5], [0, 0, 8, 0, 9, 7, 0, 0, 0], [6, 0, 2, 0, 0, 0, 0, 0, 4],
     [1, 0, 0, 0, 2, 0, 0, 0, 7], [5, 0, 0, 0, 0, 0, 3, 0, 6], [0, 0, 0, 0, 6, 0, 0, 0, 0], [2, 0, 0, 0, 0, 4, 5, 3, 8],
     [0, 0, 0, 5, 3, 0, 2, 0, 0]]
    print(valid(board10, (2,6), 4))
    board3 = maker()
    printBoard(board3)
    print(solve(board3))
    print("\n\n\n\n")
    printBoard(board3)
    print(checkBoard(board3))
    print(solve(board3))






