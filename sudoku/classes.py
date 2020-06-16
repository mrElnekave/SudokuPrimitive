import pygame
from sudoku import constants as cst
from sudoku.Generators import sudGen
from sudoku.solvers import SudokuSolve


class Tile:

    def __init__(self, num=0, isOrig=False):
        self.img = "pics/num" + str(num) + ".png"
        self.x = 0
        self.y = 0
        self.val = num
        self.isOrig = isOrig
        self.Image = pygame.image.load(self.img)

    def updatePos(self, row, col):
        self.y = cst.GRID_LEFT_OFFSET + row * (cst.TILE_WIDTH + cst.TILE_X_SPACER)
        self.x = cst.GRID_TOP_OFFSET + col * (cst.TILE_HEIGHT + cst.TILE_Y_SPACER)

    def switch(self, newNum: int):
        self.img = "pics/num" + str(newNum) + ".png"
        self.val = newNum
        self.updateImage()

    def updateImage(self):
        self.Image = pygame.image.load(self.img)

    def display(self):
        self.Image = pygame.transform.scale(self.Image, (cst.TILE_WIDTH - 4, cst.TILE_HEIGHT - 4))
        tileImage = pygame.image.load("pics/num0.png")
        tileImage = pygame.transform.scale(tileImage, (cst.TILE_WIDTH - 4, cst.TILE_HEIGHT - 4))
        if self.isOrig:
            tileImage.set_alpha(150)
            pass
        cst.screen.blit(tileImage, (self.x + 2, self.y + 2))
        cst.screen.blit(self.Image, (self.x + 2, self.y + 2))


class Board:
    def __init__(self):
        self.grid = [
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile(), Tile()] ]
        self.basicBoard = sudGen.getSudoku()
        self.setGrid()
    def change(self, loc, newNum):
        if(SudokuSolve.valid(self.basicBoard, loc, newNum) or newNum == 0):
            self.basicBoard[loc[0]][loc[1]] = newNum
            self.grid[loc[0]][loc[1]].switch(newNum)
        else:
            return False
            pass
    def setGrid(self):
        # nb = sudokuGen2.make()
        nb = self.basicBoard
        for row in range(len(nb)):
            for col in range(len(nb)):
                if nb[row][col] != 0:  # random.randrange(2, 5) != 4 and
                    self.grid[row][col] = Tile(nb[row][col], True)
                self.grid[row][col].updatePos(row, col)

    def display(self):
        for tiles in self.grid:
            for tile in tiles:
                tile.display()