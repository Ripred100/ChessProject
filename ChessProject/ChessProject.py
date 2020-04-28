
import sys, pygame

class Board:
    def __init__():
        rows = []
        for x in range(8):
            rows[x] = None
    def newGame():
        pass
class Piece:
    def __init__(self):
        hasMoved = False
        posMoves = []
        #posMoves is a list of possible moves for the piece. The notation is in the form of a vector and a modifyer, [x,y,modifier]
        #the modifier denotes wether the move is only available forward (f), or only if the piece hasnt moved yet (m). default is (d).
        #the x and y vectors can be set = "n" if the move doesnt have limited range like a bishop's or a rook.
        #IMPORTANT NOTE::: Do not double list vectors that are the same, just mirorred. 
        #When a move can be made to the right, and the left, only list the one going to the right (Positive y and x values)
        position = [None,None]
        #position coordinates are row, column starting from 0 to 7, starting with the bottom left corner
        #E.G. bottom left corner is 0,0, top right is 7,7 
        specialMoves = []
        #things like castling and en passant, maybe i'll add the pawn eating diagonally here

    def getMoves():
        return [posMoves, specialMoves]

class Pawn(Piece):
    def __init__(self):
        self.posMoves = [[0,1]]
    def getPosMoves():
        if self.position[0]
class Rook(Piece):
    pass
class Knight(Piece):
    pass
class Bishop(Piece):
    pass
class King(Piece):
    pass
class Queen(Piece):
    pass