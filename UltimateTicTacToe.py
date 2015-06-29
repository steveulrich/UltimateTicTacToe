import pygame

pygame.init()

########
##TO DO#
########
#--Place a large X or O over a beaten board

#Screen Properties
width = 540
height = 540
screen = pygame.display.set_mode([width, height])

#Single Board class
#Used for each of the smaller boards as well as the main large board
class Board():
    def __init__(self,position):

        #0 1 2
        #3 4 5
        #6 7 8
        self.boardList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.position = position
        self.winner = 9
        self.iterator = 0

#Sprite functions
def make_sprite (filename):
    sprite = pygame.sprite.Sprite ()
    image = pygame.image.load (filename)
    sprite.image = image.convert_alpha ()
    sprite.rect = sprite.image.get_rect ()
    sprite.mask = pygame.mask.from_surface (sprite.image)
    return sprite

def draw_sprite (sprite, pos):
    screen.blit (sprite.image, pos)

font = pygame.font.Font (pygame.font.get_default_font (), 12)

def draw_text (string, x, y):
    surf = font.render (string, True, [255, 255, 255])
    rect = surf.get_rect ()
    rect.topleft = (x, y)
    screen.blit (surf, rect)

#Game Sprites
gameboard = make_sprite("gameboard.png") #GameBoard
title = make_sprite("title.png") #Title Sprite
xSmallSprite = make_sprite("gameSmallX.png") #Small X
xBigSprite = make_sprite("gameBigX.png") #Big X
oSmallSprite = make_sprite("gameSmallO.png") #O Sprite
oBigSprite = make_sprite("gameBigO.png") #O Sprite
startButton = make_sprite("startButton.png") #Start Button
newGameButton = make_sprite("newGameButton.png") #New Game
quitButton = make_sprite("quitButton.png") #Quit
point = make_sprite("point.png") #1 pixel hit area for mouse detection

gameOverTitle = make_sprite("gameOver.png")
quitGameOver = make_sprite("quitGameOver.png")
menuButton = make_sprite("menuButton.png")
boardHighlight = make_sprite("boardHighlight.png")

inGame = False #Boolean for our game loop
running = True #Boolean for the program loop
gameOver = False

#Initialize all the small boards
#0 1 2
#3 4 5
#6 7 8
topLeft = Board(0)
topMid = Board(1)
topRight = Board(2)
botLeft = Board(6)
botMid = Board(7)
botRight = Board(8)
midLeft = Board(3)
midMid = Board(4)
midRight = Board(5)

mainBoard = Board(9)

#Put all the small boards into an array
#0 1 2
#3 4 5
#6 7 8
smallBoards = [topLeft, topMid, topRight, midLeft, midMid, midRight, botLeft, botMid, botRight]
currentSmallBoardCoordinates = [0, 0]
#9 = null for our purposes
winner = 9

playerTurn = True #True = x, False = o
smallBoardIndex = 9
allowedBoard = 9

allCurrentXO = pygame.sprite.Group()
firstTurn = True

#Check the horizontal indeces of the board
def HorizontalCheck(passedBoard):
    #Look at the internal array of the passedBoard
    board = passedBoard.boardList
    #Check that there are consecutive horizontal values
    #0 1 2
    #3 4 5
    #6 7 8
    if board[0] == board[1] and board[0] == board[2]:
        passedBoard.winner = board[0]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    elif board[3] == board[4] and board[3] == board[5]:
        passedBoard.winner = board[3]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    elif board[6] == board[7] and board[6] == board[8]:
        passedBoard.winner = board[6]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    return False

#Check the vertical indexes of the board
def VerticalCheck(passedBoard):
    #Look at the internal array of the passedBoard
    board = passedBoard.boardList
    #Check that there are consecutive vertical values
    #0 1 2
    #3 4 5
    #6 7 8
    if board[0] == board[3] and board[0] == board[6]:
        passedBoard.winner = board[0]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    elif board[1] == board[4] and board[1] == board[7]:
        passedBoard.winner = board[1]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    elif board[2] == board[5] and board[2] == board[8]:
        passedBoard.winner = board[2]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    return False

#Check for a win diagonally
def DiagonalCheck(passedBoard):
    #Look at the internal array of the passedBoard
    board = passedBoard.boardList
    #Check that there are consecutive diagonal values
    #0 1 2
    #3 4 5
    #6 7 8
    if board[0] == board[4] and board[0] == board[8]:
        passedBoard.winner = board[0]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
            
        return True
    elif board[6] == board[4] and board[6] == board[2]:
        passedBoard.winner = board[6]
        if passedBoard.winner == True:
            print "X won board " + str(passedBoard.position)
        elif passedBoard.winner == False:
            print "O won board " + str(passedBoard.position)
        return True
    return False

#Check if a small board has been won
def CheckWinSmall(smallBoard):
    if HorizontalCheck(smallBoard):
        mainBoard.boardList[smallBoard.position] = smallBoard.winner
        #Display a large O or X over the won small board
    elif VerticalCheck(smallBoard):
        mainBoard.boardList[smallBoard.position] = smallBoard.winner
        #Display a large O or X over the won small board
    elif DiagonalCheck(smallBoard):
        mainBoard.boardList[smallBoard.position] = smallBoard.winner
        #Display a large O or X over the won small board

#Call this to check the main board
def CheckWinMain():
    if(mainBoard.winner == 9):
        if HorizontalCheck(mainBoard):
            global winner
            winner = mainBoard.winner
            global gameOver
            gameOver = True
            global inGame
            inGame = False
            if winner == True: #X Wins
                print "X WINS by Horizontal!"
            elif winner == False: #O Wins
                print "O WINS by Horizontal!"
        elif VerticalCheck(mainBoard):
            global winner
            winner = mainBoard.winner
            global gameOver
            gameOver = True
            global inGame
            inGame = False
            if winner == True: #X Wins
                print "X WINS by Horizontal!"
            elif winner == False: #O Wins
                print "O WINS by Horizontal!"
        elif DiagonalCheck(mainBoard):
            global winner
            winner = mainBoard.winner
            global gameOver
            gameOver = True
            global inGame
            inGame = False
            if winner == True: #X Wins
                print "X WINS by Horizontal!"
            elif winner == False: #O Wins
                print "O WINS by Horizontal!"

#Call this to iterate through all small boards
def CheckSmallBoards():
    for board in smallBoards:
        if(board.winner == 9):
            CheckWinSmall(board)

#Resets the boardList of all boards
def ResetGame():
    global topLeft
    topLeft = Board(0)

    global topMid
    topMid = Board(1)

    global topRight
    topRight = Board(2)

    global botLeft
    botLeft = Board(6)

    global botMid
    botMid = Board(7)

    global botRight
    botRight = Board(8)

    global midLeft
    midLeft = Board(3)
    
    global midMid
    midMid = Board(4)

    global midRight
    midRight = Board(5)

    global mainBoard
    mainBoard = Board(9)

    #Put all the small boards into an array
    #0 1 2
    #3 4 5
    #6 7 8
    global smallBoards
    smallBoards = [topLeft, topMid, topRight, midLeft, midMid, midRight, botLeft, botMid, botRight]
    global winner
    winner = 9

    global playerTurn
    playerTurn = True
    
    allCurrentXO.empty()

#used to get an index for the smallboard we are currently playing in            
def WhatSmallBoardAreWeIn(row, column):
    if(column == 0 or column == 1 or column == 2):
        if(row == 0 or row == 1 or row == 2):
            return 0
        elif(row == 3 or row == 4 or row == 5):
            return 1
        elif(row == 6 or row == 7 or row == 8):
            return 2
    if(column == 3 or column == 4 or column == 5):
        if(row == 0 or row == 1 or row == 2):
            return 3
        elif(row == 3 or row == 4 or row == 5):
            return 4
        elif(row == 6 or row == 7 or row == 8):
            return 5
    if(column == 6 or column == 7 or column == 8):
        if(row == 0 or row == 1 or row == 2):
            return 6
        elif(row == 3 or row == 4 or row == 5):
            return 7
        elif(row == 6 or row == 7 or row == 8):
            return 8

#used to get an index for the next smallboard we are allowed to play in
def NextSmallBoardAllowed(row, column):
    if(column == 0 or column == 3 or column == 6):
        if(row == 0 or row == 3 or row == 6):
            return 0
        elif(row == 1 or row == 4 or row == 7):
            return 3
        elif(row == 2 or row == 5 or row == 8):
            return 6
        
    elif(column == 1 or column == 4 or column == 7):
        if(row == 0 or row == 3 or row == 6):
            return 1
        elif(row == 1 or row == 4 or row == 7):
            return 4
        elif(row == 2 or row == 5 or row == 8):
            return 7
        
    elif(column == 2 or column == 5 or column == 8):
        if(row == 0 or row == 3 or row == 6):
            return 2
        elif(row == 1 or row == 4 or row == 7):
            return 5
        elif(row == 2 or row == 5 or row == 8):
            return 8

#Highlights the smallboard the player is allowed to make a move on
def UpdateCurrentHighlightedBoard(row, column):
    if(column == 0 or column == 3 or column == 6):
        if(row == 0 or row == 3 or row == 6):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [0, 0]
        elif(row == 1 or row == 4 or row == 7):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [0, 180]
        elif(row == 2 or row == 5 or row == 8):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [0, 360]
        
    elif(column == 1 or column == 4 or column == 7):
        if(row == 0 or row == 3 or row == 6):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [180, 0]
        elif(row == 1 or row == 4 or row == 7):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [180, 180]
        elif(row == 2 or row == 5 or row == 8):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [180, 360]
        
    elif(column == 2 or column == 5 or column == 8):
        if(row == 0 or row == 3 or row == 6):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [360, 0]
        elif(row == 1 or row == 4 or row == 7):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [360, 180]
        elif(row == 2 or row == 5 or row == 8):
            global currentSmallBoardCoordinates
            currentSmallBoardCoordinates = [360, 360]

        
###########
###########
###########
#Game Loop#
###########        
###########
###########
        
while running:
    draw_sprite(gameboard, gameboard.rect)
    allCurrentXO.draw(screen)
    
    #Check for game over
    if inGame == True:
        if(firstTurn == False):
            boardHighlight.rect = currentSmallBoardCoordinates
            draw_sprite(boardHighlight, boardHighlight.rect)
        CheckWinMain()
        CheckSmallBoards()
    elif gameOver == True:
        draw_sprite(gameOverTitle, gameOverTitle.rect)
        draw_sprite(quitGameOver, quitGameOver.rect)
        draw_sprite(menuButton, menuButton.rect)
    elif inGame == False:
        draw_sprite(title, title.rect)
        draw_sprite(startButton, startButton.rect)
        draw_sprite(quitButton, quitButton.rect)
        
    #PyGame Events
    for event in pygame.event.get():
        
        #Closing the window stops the program
        if event.type == pygame.QUIT:
            running = False

        #If the player clicks on the screen
        elif event.type ==  pygame.MOUSEBUTTONDOWN:
            point.rect.topleft = event.pos #Move our point to the spot we clicked
            if gameOver == True:
                if pygame.sprite.collide_mask(point, menuButton):
                    global gameOver
                    gameOver = False
                    ResetGame()
                elif pygame.sprite.collide_mask(point, quitGameOver):
                    running = False
            elif inGame == False:
                #Clicked the start game button?
                if pygame.sprite.collide_mask(point, startButton):
                    global inGame
                    inGame = True
                    global firstTurn
                    firstTurn = True
                    allowedBoard = 9
                #Clicked quit?
                elif pygame.sprite.collide_mask(point, quitButton):
                    running = False

            elif inGame == True:
                #column will = 0-8
                gridColumn = event.pos[0] / 60
                #row will = 0-8
                gridRow = event.pos[1] / 60
                
                smallBoardIndex = WhatSmallBoardAreWeIn(gridColumn, gridRow)

                #If it's the first move of the game, player can go anywhere
                if firstTurn == True:
                    allowedBoard = smallBoardIndex
                    firstTurn = False
                    
                #Check the smallboardIndex the person clicked in against the board they are allowed to place in
                if smallBoardIndex == allowedBoard:
                    if playerTurn == True:
                        tempAllowedBoard = NextSmallBoardAllowed(gridRow, gridColumn)
                        if(smallBoards[smallBoardIndex].boardList[tempAllowedBoard] == tempAllowedBoard): 
                            x = make_sprite("gameSmallX.png") #Small X
                            x.rect = [gridColumn * 60, gridRow * 60]
                            allCurrentXO.add(x)
                            allowedBoard = NextSmallBoardAllowed(gridRow, gridColumn)
                            UpdateCurrentHighlightedBoard(gridRow, gridColumn)
                            smallBoards[smallBoardIndex].boardList[allowedBoard] = playerTurn
                            global playerTurn
                            playerTurn = False
                        else:
                            print "That spot is taken by an O!"
                    elif playerTurn == False:
                        tempAllowedBoard = NextSmallBoardAllowed(gridRow, gridColumn)
                        if(smallBoards[smallBoardIndex].boardList[tempAllowedBoard] == tempAllowedBoard):                         
                            o = make_sprite("gameSmallO.png") #Small O
                            o.rect = [gridColumn * 60, gridRow * 60]
                            allCurrentXO.add(o)
                            allowedBoard = NextSmallBoardAllowed(gridRow, gridColumn)
                            UpdateCurrentHighlightedBoard(gridRow, gridColumn)
                            smallBoards[smallBoardIndex].boardList[allowedBoard] = playerTurn
                            global playerTurn
                            playerTurn = True
                        else:
                            print "That spot is taken by an X!"
                        
                else:
                    print "Small board != allowedBoard!"
    
    pygame.display.flip()
pygame.quit()  
