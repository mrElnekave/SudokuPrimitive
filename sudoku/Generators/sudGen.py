import random
from sudoku import constants as cst
easy = [
[
    [0, 5, 0, 8, 4, 9, 0, 3, 0] ,
    [0, 0, 0, 0, 0, 0, 0, 4, 0] ,
    [0, 0, 0, 0, 0, 5, 0, 1, 2] ,
    [8, 0, 0, 0, 0, 0, 0, 5, 0] ,
    [6, 0, 9, 0, 5, 0, 2, 0, 3] ,
    [0, 7, 0, 0, 0, 0, 0, 0, 1] ,
    [5, 8, 0, 6, 0, 0, 0, 0, 0] ,
    [0, 6, 0, 0, 0, 0, 0, 0, 0] ,
    [0, 2, 0, 9, 1, 7, 0, 8, 0] ,
],
[
    [0, 7, 0, 5, 0, 2, 0, 0, 0] ,
    [0, 0, 0, 0, 0, 0, 8, 7, 0] ,
    [5, 3, 0, 1, 4, 0, 0, 0, 0] ,
    [0, 6, 5, 0, 0, 8, 0, 0, 0] ,
    [0, 0, 1, 0, 0, 0, 3, 0, 0] ,
    [0, 0, 0, 7, 0, 0, 6, 4, 0] ,
    [0, 0, 0, 0, 3, 4, 0, 1, 7] ,
    [0, 8, 9, 0, 0, 0, 0, 0, 0] ,
    [0, 0, 0, 6, 0, 9, 0, 8, 0] ,
],
[
    [4, 0, 0, 0, 0, 7, 0, 1, 3] ,
    [1, 6, 0, 4, 0, 0, 5, 0, 0] ,
    [3, 0, 0, 9, 0, 0, 0, 0, 0] ,
    [0, 8, 2, 0, 7, 0, 0, 0, 0] ,
    [0, 5, 0, 0, 3, 0, 0, 9, 0] ,
    [0, 0, 0, 0, 9, 0, 4, 8, 0] ,
    [0, 0, 0, 0, 0, 5, 0, 0, 4] ,
    [0, 0, 3, 0, 0, 8, 0, 6, 5] ,
    [5, 4, 0, 3, 0, 0, 0, 0, 7] ,
],
]

medium = [
[
    [0, 0, 0, 0, 4, 5, 0, 7, 6] ,
    [0, 4, 0, 3, 0, 0, 1, 0, 0] ,
    [7, 2, 0, 0, 0, 0, 0, 0, 0] ,
    [0, 6, 0, 0, 0, 2, 0, 3, 7] ,
    [0, 0, 0, 0, 0, 0, 0, 0, 0] ,
    [2, 3, 0, 9, 0, 0, 0, 5, 0] ,
    [0, 0, 0, 0, 0, 0, 0, 6, 3] ,
    [0, 0, 2, 0, 0, 7, 0, 4, 0] ,
    [9, 1, 0, 4, 3, 0, 0, 0, 0] ,
],
[
    [0, 0, 0, 3, 0, 4, 0, 8, 9] ,
    [0, 9, 3, 0, 0, 0, 0, 7, 2] ,
    [0, 2, 0, 0, 0, 0, 0, 0, 0] ,
    [0, 4, 0, 8, 6, 0, 3, 0, 7] ,
    [0, 0, 0, 0, 1, 0, 0, 0, 0] ,
    [5, 0, 8, 0, 9, 3, 0, 4, 0] ,
    [0, 0, 0, 0, 0, 0, 0, 1, 0] ,
    [9, 5, 0, 0, 0, 0, 7, 2, 0] ,
    [4, 7, 0, 1, 0, 9, 0, 0, 0] ,
],
[
    [0, 0, 0, 9, 4, 0, 6, 7, 0] ,
    [0, 0, 5, 0, 0, 0, 0, 0, 0] ,
    [2, 0, 0, 0, 1, 0, 0, 5, 3] ,
    [0, 0, 6, 7, 0, 0, 0, 1, 5] ,
    [0, 0, 2, 0, 0, 0, 7, 0, 0] ,
    [7, 8, 0, 0, 0, 0, 4, 0, 0] ,
    [6, 7, 0, 0, 2, 0, 0, 0, 4] ,
    [0, 0, 0, 0, 0, 0, 2, 0, 0] ,
    [0, 2, 1, 0, 6, 7, 0, 0, 0] ,
],
]

unknown = [
    [
        [0, 0, 8, 1, 0, 0, 0, 9, 0],
        [0, 0, 9, 0, 0, 2, 0, 0, 0],
        [0, 0, 3, 0, 0, 7, 6, 0, 2],
        [1, 7, 0, 8, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [5, 0, 0, 0, 0, 4, 0, 7, 8],
        [9, 0, 1, 4, 0, 0, 2, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 0],
        [0, 6, 0, 0, 0, 1, 4, 0, 0]
    ],
    [
        [0, 4, 0, 0, 0, 2, 3, 8, 0],
        [0, 0, 0, 0, 6, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 9, 0],
        [0, 9, 1, 0, 8, 0, 0, 0, 0],
        [4, 0, 0, 0, 1, 0, 0, 0, 6],
        [0, 0, 0, 0, 2, 0, 8, 4, 0],
        [0, 1, 0, 0, 0, 0, 5, 7, 0],
        [0, 0, 0, 0, 9, 0, 0, 0, 0],
        [0, 3, 9, 5, 0, 0, 0, 1, 0]
    ],
    [
        [0, 7, 0, 2, 0, 0, 0, 6, 5],
        [0, 0, 0, 0, 0, 0, 0, 8, 0],
        [0, 0, 2, 0, 5, 0, 4, 0, 1],
        [0, 8, 0, 0, 0, 5, 0, 0, 0],
        [7, 0, 6, 0, 0, 0, 1, 0, 4],
        [0, 0, 0, 6, 0, 0, 0, 7, 0],
        [4, 0, 9, 0, 3, 0, 6, 0, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 0],
        [1, 3, 0, 0, 0, 9, 0, 2, 0]
    ]
]

def getSudoku():

    boards = [
        easy,
        medium,
        unknown
    ]

    board = boards[cst.difficulty]
    length = len(board)
    # board = board[int(random.random() * length)]
    board =  [
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
    lineFlips = int(random.random() * 9)  # all the lines flipped
    for i in range(lineFlips):
        board = flipLinesInBlock(board)
    blockFlips = int(random.random() * 5)  # cause why not
    for i in range(blockFlips):
        board = flipBlocks(board)
    rotations = int(random.random() * 4)  # 4 possible rotations
    for i in range(rotations):
        board = rotateBoardClockwise(board)
    times = int(random.random() * 9)  # 9 numbers in Sudoku
    board = incrementAll(board, times)
    return board


def flipLinesInBlock(board):  # this can only occur to lines in blocks to preserve all 9 numbers in that block

    if(random.randint(0, 1) == 0):  # row flipping
        box = int(random.random() * 3) * 3
        row1 = int(random.random() * 3) + box
        row2 = int(random.random() * 3) + box
        temp = board[row1]
        board[row1] = board[row2]
        board[row2] = temp
    else:  # column flipping -- bad --
        board = rotateBoardClockwise(board)
        box = int(random.random() * 3) * 3
        col1 = int(random.random() * 3) + box
        col2 = int(random.random() * 3) + box
        temp = board[col1]
        board[col1] = board[col2]
        board[col2] = temp

    return board


def flipBlocks(board):  # flip the blocks altogether preserving everything else
    row1 = int(random.random() * 3) * 3
    row2 = int(random.random() * 3) * 3
    if random.randint(0, 1) == 1:
        rotateBoardClockwise(board)
    for i in range(3):
        temp = board[row1 + i]
        board[row1 + i] = board[row2 + i]
        board[row2 + i] = temp

    return board


def incrementAll(board,times):
  for i in range(9):
    for j in range(9):
      if (board[i][j] > 0):
        board[i][j] = board[i][j] + times
        if (board[i][j] > 9):
          board[i][j] = board[i][j] - 9

  return board


def rotateBoardClockwise(board):
    newBoard = [0,0,0,0,0,0,0,0,0]
    for row in range(9):
        newBoard[row] = [0,0,0,0,0,0,0,0,0]
        for col in range(9):
          newBoard[row][col] = board[col][row]


    for row in range(9):
        newBoard[row].reverse()

    return newBoard


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
    print(" A sudoku is generated by mixing up previously generated sudokus \n")
    board3 = getSudoku()
    printBoard(board3)
