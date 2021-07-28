from Chip import Chip

class Board:
    BoardArray = []
    def __init__(self):
        self.BoardArray = [[Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("A"),Chip("B"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("B"),Chip("A"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")],
                      [Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_"),Chip("_")]]

    def getWinner(self):
        intA = 0
        for i in range(8):
            for j in range(8):
                intA = intA + 1
        
        if intA == 32:
            return "DRAW"
        elif intA > 32:
            return "Player A wins!!!"
        else:
            return "Player B wins!!!"

    def __str__(self):
        strRet = "   0  1  2  3  4  5  6  7\n"
        for i in range(8):
            strRet += str(i) + " "
            for j in range(8):
                strRet += " " + self.BoardArray[i][j].getState() + " "
            strRet += "\n"
        return strRet