
import sys, pygame
pygame.init()

displayWidth = 800
displayHeight = 800

black = (0,0,0)
white = (255,255,255)

x = Board()

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
        
    def newGame():
        for x in positions:
            for n in x:
                del n
                n = None


        positions[0][0] = Rook("white",[0,0])
        positions[0][1] = Knight("white",[0,1])
        positions[0][2] = Bishop("white",[0,2])
        positions[0][3] = King("white",[0,3])
        positions[0][4] = Queen("white",[0,4])
        positions[0][5] = Bishop("white",[0,5])
        positions[0][6] = Rook("white",[0,6])
        positions[0][7] = Knight("white",[0,7])

        positions[7][0] = Rook("black",[7,0])
        positions[7][1] = Knight("black",[7,1])
        positions[7][2] = Bishop("black",[7,2])
        positions[7][3] = King("black",[7,3])
        positions[7][4] = Queen("black",[7,4])
        positions[7][5] = Bishop("black",[7,5])
        positions[7][6] = Rook("black",[7,6])
        positions[7][7] = Knight("black",[7,7])


class Piece:
    def __init__(self,side,position):
        hasMoved = False
        posMoves = [[1,1],[1,2]]

        #posMoves is a list of possible moves for the piece. The notation is in the form of a vector and a modifyer, [x,y,modifier]
        #the modifier denotes wether the move is only available forward (f), or only if the piece hasnt moved yet (m). default is (d).
        #the x and y vectors can be set = "n" if the move doesnt have limited range like a bishop's or a rook.
        #IMPORTANT NOTE::: Do not double list vectors that are the same, just mirorred. 
        #When a move can be made to the right, and the left, only list the one going to the right (Positive y and x values)

        position = [0,0]
        #position coordinates are column, row starting from 0 to 7, starting with the bottom left corner
        #E.G. bottom left corner is 0,0, top right is 7,7. It behaves like an x,y plane

        specialMoves = []
        #things like castling and en passant, maybe i'll add the pawn eating diagonally here

        side = None
        #"white" or "black"

    def getMoves():
        return posMoves
    def getSpecialMoves():
        return specialMoves
    def getPosition():
        return position

    def getCurrentMoves():
        i = 0
        currentMoves = []
        for x in getMoves():
            while (i < len(x)):
                newSpace[i] = x[i] + getposition()[i]
                i = i+1
            currentMoves.append(newSpace)
        return(currentMoves)

#class Pawn(Piece):
#    pass
#class Rook(Piece):
#    pass
#class Knight(Piece):
#    pass
#class Bishop(Piece):
#    pass
#class King(Piece):
#    pass
#class Queen(Piece):
#    pass

