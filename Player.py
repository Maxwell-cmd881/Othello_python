class Player:
    Symbol = ""
    def __init__(self,symbol):
        self.Symbol = symbol


    def makeMove(self,Arena,iTarget,jTarget):
        
        if Arena.BoardArray[iTarget][jTarget].getState() != "_":
            return True
        
        North = False
        East = False
        South = False
        West = False
        NorthEast = False
        SouthEast = False
        SouthWest = False
        NorthWest = False
        

        
        #north
        i = iTarget -1
        j = jTarget
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for n in range(i,iTarget):
                    Arena.BoardArray[n][j].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                North = True
                break

            i = i -1

        #South
        i = iTarget +1
        j = jTarget
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for n in range(iTarget,i):
                    Arena.BoardArray[n][j].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                South = True
                break

            i = i +1

        #east
        i = iTarget
        j = jTarget+1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for n in range(jTarget,j):
                    Arena.BoardArray[i][n].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                East = True
                break

            j = j +1

        #west
        i = iTarget
        j = jTarget-1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for n in range(j,jTarget):
                    Arena.BoardArray[i][n].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                West = True
                break

            j = j -1

        #NorthEast--------test more later
        i = iTarget-1
        j = jTarget+1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for k in range (iTarget-i):
                    Arena.BoardArray[iTarget - k][jTarget + k].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                NorthEast = True
                break

            j = j +1
            i = i -1

        #SouthWest--------test more later
        i = iTarget+1
        j = jTarget-1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for k in range(i - iTarget):
                    Arena.BoardArray[iTarget + k][jTarget - k].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                SouthWest = True
                break

            j = j -1
            i = i +1

        #NorthWest--------test more later
        i = iTarget-1
        j = jTarget-1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for k in range(iTarget - i):
                    Arena.BoardArray[iTarget -k][jTarget - k].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                NorthWest = True
                break

            j = j -1
            i = i -1

        #SouthEast--------test more later
        i = iTarget+1
        j = jTarget+1
        while (i >= 0 and i < 8 and j >=0 and j < 8):
            if Arena.BoardArray[i][j].getState() == "_":
                break
            
            if Arena.BoardArray[i][j].getState() == self.Symbol:
                for k in range(i- iTarget):
                    Arena.BoardArray[iTarget + k][jTarget + k].setState(self.Symbol)
                Arena.BoardArray[iTarget][jTarget].setState(self.Symbol)
                SouthEast = True
                break

            j = j +1
            i = i +1

        if(North or NorthEast or East or SouthEast or South or SouthWest or West or NorthWest):
            print("move Succsesful!")
        else:
            return True