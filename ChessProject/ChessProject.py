
import sys, pygame
pygame.init()


displayWidth = 800
displayHeight = 800

black = (0,0,0)
white = (255,255,255)


def addArr(pos,move):
    x = pos[0] + move[0]
    y = pos[1] + move[1]
    return [x,y]


class Board:
    def __init__(self):
        self.positions = [[[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]],
                [[1],[2],[3],[4],[5],[6],[7],[8]]]
        Board.newGame(self)
        
    def newGame(self):
        for x in self.positions:
            for n in x:
                del n
                n = None

        self.positions[0][0] = Rook("white",[0,0])
        self.positions[0][1] = Knight("white",[0,1])
        self.positions[0][2] = Bishop("white",[0,2])
        self.positions[0][3] = King("white",[0,3])
        self.positions[0][4] = Queen("white",[0,4])
        self.positions[0][5] = Bishop("white",[0,5])
        self.positions[0][6] = Rook("white",[0,6])
        self.positions[0][7] = Knight("white",[0,7])

        for i in range(8):
            self.positions[1][i] = Pawn("white",[1,i])

        self.positions[7][0] = Rook("black",[7,0])
        self.positions[7][1] = Knight("black",[7,1])
        self.positions[7][2] = Bishop("black",[7,2])
        self.positions[7][3] = King("black",[7,3])
        self.positions[7][4] = Queen("black",[7,4])
        self.positions[7][5] = Bishop("black",[7,5])
        self.positions[7][6] = Rook("black",[7,6])
        self.positions[7][7] = Knight("black",[7,7])

        for i in range(8):
            self.positions[6][i] = Pawn("black",[6,i])

    def getPieceInPosition(self,column, row):
        return self.positions[column][row]
class Piece:
    def __init__(self,side,position):
        self.hasMoved = False
        self.posMoves = [[1,1],[1,2]]

        #posMoves is a list of possible moves for the piece. Currently, just a vector of all possible moves TO DO: The notation is in the form of a vector and a modifyer, [x,y,modifier]
        #the modifier denotes wether the move is only available forward (f), or only if the piece hasnt moved yet (m). default is (d).
        #the x and y vectors can be set = "n" if the move doesnt have limited range like a bishop's or a rook.
        #IMPORTANT NOTE::: Do not double list vectors that are the same, just mirorred. 
        #When a move can be made to the right, and the left, only list the one going to the right (Positive y and x values)

        self.position = position
        #position coordinates are column, row starting from 0 to 7, starting with the bottom left corner
        #E.G. bottom left corner is 0,0, top right is 7,7. It behaves like an x,y plane

        self.specialMoves = []
        #things like castling and en passant, maybe i'll add the pawn eating diagonally here

        self.side = side
        #"white" or "black"

    def getMoves(self):
        return self.posMoves
    def getSpecialMoves(self):
        return self.specialMoves
    def getPosition(self):
        return self.position
    def __repr__(self):
        return (f"i am a {self.side} {type(self)} in position {self.getPosition()}")

    def getCurrentMoves(self):
        currentMoves = []
        validMoves = []
        for x in self.getMoves():
            currentMoves.append(addArr(self.getPosition(),x))

        for x in currentMoves:
            if x[0] < 8 and x[0] >= 0 and  x[1] < 8 and x[1] >= 0:
                validMoves.append(x)
        return validMoves
            
       

class Pawn(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = True
        self.posMoves = [[0,1]]
        #Variable
        self.side = side
        self.position = position
class Rook(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = False
        self.posMoves = [[0,1],[1,0]]
        #Variable
        self.side = side
        self.position = position
class Knight(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = True
        self.posMoves = [[2,1],[1,2]]
        #Variable
        self.side = side
        self.position = position
class Bishop(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = False
        self.posMoves = [[1,1]]
        #Variable
        self.side = side
        self.position = position
class King(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = True
        self.posMoves = [[0,1],[1,0]]
        #Variable
        self.side = side
        self.position = position
class Queen(Piece):
    def __init__(self,side,position):
        #constants
        self.hasMoved = False
        self.finiteMovement = False
        self.posMoves = [[1,1],[1,0],[0,1]]
        #Variable
        self.side = side
        self.position = position

x = Board()

print(x.getPieceInPosition(0,0).getCurrentMoves())
