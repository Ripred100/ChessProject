
import sys, pygame
pygame.init()

size = width, height = 512, 512
turn = 0
black = 0, 0, 0

screen = pygame.display.set_mode(size)


class Piece:
    
    possibleMoves = [None]

class Rook(Piece):
    #placeholder

class Pawn(Piece):
    #placeholder


class Board:
    
    positions = [row1,row2,row3,row4,row5,row6,row7,row8]

class Row:
    places = [a,b,c,d,e,f,g,h]
    def contents():





def decode():
    #will turn array adresses into readable chess board space ID's (Like E5, or A1, from 0,3, etc)


