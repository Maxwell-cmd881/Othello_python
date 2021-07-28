from Board import Board
from Player import Player
remaining = 60;
Arena = Board()

print(Arena)
player1 = Player("A")
player2 = Player("B")
while(remaining > 0):
    #playerA turn
    Aturn = True
    while Aturn:
        i = int(input("player A choose row: "))
        j = int(input("player A choose column: "))
        if (i == 111)  or (j == 111):
            break
        if player1.makeMove(Arena,i,j):
            print("invalid move. try again. to skip enter row or column 111")
        else:
            Aturn = False
            remaining = remaining - 1
        print(Arena)
    
    #playerB turn
    Bturn = True
    while Bturn:
        i = int(input("player B choose row: "))
        j = int(input("player B choose column: "))
        if (i == 111) or (j == 111):
            break
        if player2.makeMove(Arena,i,j):
            print("invalid move. try again. to skip enter row or column 111")
        else:
            Bturn = False
            remaining = remaining - 1
        print(Arena)
    
#determine winner
print("results: " + Arena.getWinner());


