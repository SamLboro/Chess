"""
This is our main driver file. It will be responsible for handling user input and displaying the current GameState object. 
"""

import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 #dimensions of a chess board are 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 #for animations later on
IMAGES = {}

'''
Initialise a global dictionary of images. This will be called exactly once in the main. 
'''

def loadImages():
  pieces = ["wp", "wR", "wN", "wB", "wK", "wQ", "bp", "bN", "bR", "bB", "bQ", "bK"]
  for piece in pieces:
    IMAGES[piece] = p.image.load("images/" + piece + ".png")
  #Note: we can access an image by saying 'IMAGES["wP"]'
  
  
  
