import pygame, sys
# from pygame import mixer
from sudoku import constants as cst
from sudoku.classes import Board
from sudoku.solvers import SudokuSolve
from enum import Enum
import time

# thank you to Tomer Sedan for helping me with the sudoku Solver
# thank you to http://www.7sudoku.com/ for supplying the Sudokus


# always start with this
pygame.init()

t0 = time.time()  # First time instance when project was run

mainClock = pygame.time.Clock()

# header of game {
pygame.display.set_caption("Yamm's Sudoku")
# icon = pygame.image.load("sudokuimg.png")
# pygame.display.set_icon(icon)

# }

# # sound
# mixer.music.load("sound.wav")
# mixer.music.play(-1)
# # specific sound
# someSound = mixer.Sound("sound.wav")
# someSound.play()





class State(Enum):
    START = 1
    PAUSED = 2
    PLAYING = 3
    GAME_OVER = 4


state = State.START

font = pygame.font.Font("freesansbold.ttf", 32)


def draw_text(text, surface, fontastix=pygame.font.SysFont(None, 20), color= (0,0,0), x=0, y=0):
    """

    :param text: what you want written
    :param surface: usually the program screen or any surface you want to draw on
    :param font: the font :)
    :param color: RGB color tuple
    :param x: Xpos
    :param y: Ypos
    :return: returns the object it drew if you want it to interact with stuff
    """

    textobj = fontastix.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
    return textrect


def draw_obj(obj, surface, x=0, y=0, size=None):
    imgobj = pygame.image.load(obj)
    if size is not None:
         imgobj = pygame.transform.scale(imgobj, size)
    # surface.blit(imgobj, (50, 50))
    imgrect = imgobj.get_rect()
    imgrect.topleft = (x, y)
    surface.blit(imgobj, imgrect)
    return imgrect


def gameOver():
    ggFont = pygame.font.Font("freesansbold.ttf", 50)
    game_over = ggFont.render("GAME OVER", True, (255, 255, 255))
    cst.screen.blit(game_over, (cst.SCREEN_WIDTH/2, cst.SCREEN_HEIGHT/2))


def updateTime():
    cst.timeElapsed = int(time.time() - t0)


def gridToDraw(loc):
    x = loc[0]
    y = loc[1]
    temp = x
    x = y * (cst.TILE_HEIGHT + cst.TILE_Y_SPACER) + cst.GRID_TOP
    y = temp * (cst.TILE_WIDTH + cst.TILE_X_SPACER) + cst.GRID_LEFT
    return [x,y]


def main_menu():
    click = False
    while True:

        # fill the screen
        cst.screen.fill((0, 0, 0))
        draw_text("ESC to quit", cst.screen, pygame.font.Font("freesansbold.ttf", 15), (255,255,255), cst.SCREEN_WIDTH-150, cst.SCREEN_HEIGHT-20)

        # draw buttons
        draw_text('main menu', cst.screen, font, (255, 255, 255), 20, 20)
        button_1 = draw_text('game', cst.screen, font, (255, 0, 0), 50, 100)
        button_2 = draw_text('options', cst.screen, font, (255, 0, 0), 50, 200)

        # get the mouse position
        mx, my = pygame.mouse.get_pos()

        # check for collisions on game/ option buttons
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()

        # click measures if mouse1 was pressed; it is reset each loop
        click = False

        # the events the player does. ex: press, move, hover, type etc.
        for event in pygame.event.get():
            # if the "X" was pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if a key was pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            # if the mouse was pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        mainClock.tick(60)


def options():
    running = True
    # click is if mouse1 was pressed
    click = False

    while running:

        # fill the screen
        cst.screen.fill((0, 0, 0))
        draw_text("ESC to go back", cst.screen, pygame.font.Font("freesansbold.ttf", 15), (255,255,255), cst.SCREEN_WIDTH-150, cst.SCREEN_HEIGHT-20)

        # draw buttons
        wordX = cst.OPTION_LEFT_ARROWKEY + cst.ARROWKEY_SIZE
        word = draw_text(cst.difficulties[cst.difficulty], cst.screen, font, (255, 0, 0), wordX, cst.ARROWKEY_Y)
        wordlen = word.width
        draw_text('options', cst.screen, font, (255, 255, 255), 20, 20)
        button_1X = cst.OPTION_LEFT_ARROWKEY
        button_1 = draw_obj('pics/left.png', cst.screen, button_1X, cst.ARROWKEY_Y, (cst.ARROWKEY_SIZE, cst.ARROWKEY_SIZE))
        button_2X = cst.OPTION_LEFT_ARROWKEY + cst.ARROWKEY_SIZE + wordlen
        button_2 = draw_obj('pics/right.png', cst.screen, button_2X, cst.ARROWKEY_Y, (cst.ARROWKEY_SIZE, cst.ARROWKEY_SIZE))

        # get the mouse position
        mx, my = pygame.mouse.get_pos()

        # check for collisions with the buttons
        def collisions():
            if button_1.collidepoint((mx, my)):
                if click:
                    if cst.difficulty != 0:
                        cst.difficulty -= 1
                    else:
                        cst.difficulty = 2
            if button_2.collidepoint((mx, my)):
                if click:
                    if cst.difficulty != 2:
                        cst.difficulty += 1
                    else:
                        cst.difficulty = 0
        collisions()

        # click reset every loop
        click = False
        for event in pygame.event.get():
            # if the "X" was pressed
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if the mouse was pressed
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            # if a key was pressed
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

        # tick speed
        mainClock.tick(300)


def game():
    global run
    run = True

    # the board where everything is heald
    board = Board()

    # The current pressed location
    currLoc = None

    # the location mouse is hovering over
    highlightLoc = None

    # if a wrong answer was put in (only checks row column and box)
    global wrong
    wrong = False
    wrongTime = 0

    # if a wrong answer was put in (checks the actual solution)
    deepTime = 0
    global deep
    deep = False

    # right or wrong color
    global deepColor
    deepColor = None

    # if mouse1 was pressed
    click = False

    # takes in a pixel location and returns the board location
    def checkPlaceOnBoard(loc: tuple):
        col = (-cst.GRID_LEFT_OFFSET + loc[0]) // (cst.TILE_WIDTH + cst.TILE_X_SPACER)
        row = (-cst.GRID_TOP_OFFSET + loc[1]) // (cst.TILE_HEIGHT + cst.TILE_Y_SPACER)
        if row < 0 or col < 0:
            return None
        if row > 8 or col > 8:
            return None
        if board.grid[row][col].isOrig:
            return None
        l = [row, col]
        return l

    def numEvent(event, loc):
        if not board.grid[loc[0]][loc[1]].isOrig:
            if event.type == pygame.KEYDOWN:
                keys = [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7,
                        pygame.K_8, pygame.K_9]
                for i in range(10):
                    if event.key == keys[i]:
                        newNum = i
                        if board.change(loc, newNum) == False:
                            global wrong
                            wrong = True
                        return


    while run:
        # always fill the screen first
        cst.screen.fill(cst.BACKGROUND_COLOR)
        mx, my = pygame.mouse.get_pos()
        draw_text("ESC to go back", cst.screen, pygame.font.Font("freesansbold.ttf", 15), x=cst.SCREEN_WIDTH-150, y=cst.SCREEN_HEIGHT-20)
        if (not SudokuSolve.find_empty(board.basicBoard)) and SudokuSolve.checkBoard(board.basicBoard):
            end = draw_text("end", cst.screen, font, x=cst.SCREEN_WIDTH/2, y=cst.SCREEN_HEIGHT/2)
            if end.collidepoint((mx, my)):
                if click:
                    run = False
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if pygame.mouse.get_pressed()[0] == 1:
                    click = True
        else:
            boardImage = pygame.image.load("pics/Empty_Sudoku_Grid.png")
            boardImage = pygame.transform.scale(boardImage, ((cst.TILE_WIDTH + cst.TILE_X_SPACER) * cst.ROWS + 6, (cst.TILE_HEIGHT + cst.TILE_Y_SPACER) * cst.COLS + 6))
            word = draw_text("deep-check", cst.screen, font, x=(cst.TILE_WIDTH + cst.TILE_X_SPACER) * cst.ROWS + 6 + cst.GRID_LEFT, y=cst.ARROWKEY_Y)


            if deep:
                if deepTime < 10:
                    deepTime += 1
                    draw_text("deep-check", cst.screen, font, color=deepColor,
                              x=(cst.TILE_WIDTH + cst.TILE_X_SPACER) * cst.ROWS + 6 + cst.GRID_LEFT,
                              y=cst.ARROWKEY_Y)
                else:
                    deepTime = 0
                    deep = False

            def collisions():
                if word.collidepoint((mx, my)):
                    if click:
                        global deepColor
                        global deep
                        if SudokuSolve.solve(board.basicBoard):  # why doesn't it make a new board
                            deepColor = (0, 255, 0)
                            deep = True

                        else:
                            deepColor = (255, 0, 0)
                            deep = True

            collisions()
            #do stuff here

            if highlightLoc != None:
                pygame.draw.rect(cst.screen, (200, 255, 0), (highlightLoc[0] - 1, highlightLoc[1] - 1, cst.TILE_WIDTH + 2, cst.TILE_HEIGHT + 2))
            if currLoc != None and not wrong:
                drawLoc = gridToDraw(currLoc)
                pygame.draw.rect(cst.screen, (0, 255, 0), (drawLoc[0] - 1, drawLoc[1] - 1, cst.TILE_WIDTH + 2, cst.TILE_HEIGHT + 2))
            if wrong:
                pygame.draw.rect(cst.screen, (255, 0, 0), (drawLoc[0] - 1, drawLoc[1] - 1, cst.TILE_WIDTH + 2, cst.TILE_HEIGHT + 2))
                wrongTime += 1
                if wrongTime == 10:
                    wrongTime = 0
                    wrong = False

            cst.screen.blit(boardImage, (cst.GRID_LEFT - 5, cst.GRID_TOP - 5))
            board.display()
            updateTime()
            click = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    sys.exit()
                if currLoc != None:
                    numEvent(event, currLoc)
                pos = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEMOTION:
                    if cst.GRID_RIGHT > pos[0] > cst.GRID_LEFT and cst.GRID_BOTTOM > pos[1] > cst.GRID_TOP:
                        highlightLoc = checkPlaceOnBoard(pos)
                        if highlightLoc != None:
                            highlightLoc = gridToDraw(highlightLoc)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                if pygame.mouse.get_pressed()[0] == 1:
                    click = True
                    currLoc = checkPlaceOnBoard(pos)


        # updates display
        pygame.display.update()
        mainClock.tick(60)



main_menu()