"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object.
"""

import pygame as p
from Chess import ChessEngine

p.init()
WIDTH = HEIGHT = 512  # 400 is another option
DIMENSION = 8  # dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15  # for animations later on
IMAGES = {}

'''
Initialise a global dictionary of images. This will be called exactly once in the main. 
'''


def loadImages():
    pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bN", "bR", "bB", "bQ", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))
    # Note: we can access an image by saying 'IMAGES["wP"]'


'''
The main driver for our code. This will handle user input and updating the graphics
'''


def main():
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    validMoves = gs.getValidMoves()
    moveMade = False #Flag variable for when a move is made

    loadImages() # only do this once, before the while loop
    running = True
    sqSelected = () #No square is selected initially, this keeps track of the last click of the user (tuple: (row, col))
    playerClicks = [] #This keeps tracks of the player clicks (two tuples: [(6, 4), (4, 4)]


    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            #Mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() #This is the (x,y) location of the mouse.
                col = location[0]//SQ_SIZE
                row = location[1]//SQ_SIZE
                if sqSelected == (row, col): #The user clicked the same square twice
                    sqSelected = () #Deselect the square
                    playerClicks = [] #Clear the player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) #We append for both first and second clicks.

                if len(playerClicks) == 2: #This is after the second click
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    print(move.getChessNotation())
                    if move in validMoves:
                        gs.makeMove(move)
                        moveMade = True
                    sqSelected = () #Reset the user clicks
                    playerClicks = [] #Reset the history
            #Key handlers
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: #undo when z is pressed
                    gs.undoMove()
                    moveMade = True

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all the graphics within the current game state.
'''
def drawGameState(screen, gs):
    drawBoard(screen) #Draw the squares on the board
    drawPieces(screen, gs.board) #Draw pieces on top of those squares

'''
Draw the squares on the board.
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r+c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



'''
Draw the pieces on the board using the current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != "--": #Means it's not an empty square.
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))



if __name__ == "__main__":
    main()
