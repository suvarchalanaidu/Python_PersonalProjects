board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

player= "X"
gameon=True
gamewon= True

def drawboard(board):
    print(board[0]+"|"+board[1]+"|"+board[2])
    print("======")
    print(board[3]+"|"+board[4]+"|"+board[5])
    print("======")
    print(board[6]+"|"+board[7]+"|"+board[8])
#drawboard(board)

def askuserinput(board):
    userinp = int(input("Enter any number from 1 to 9: "))
    if(userinp >=1 or userinp <=9 and board[userinp-1]!="X"):
        board[userinp-1]=player
    else:
        print("Invalid input or already played there")

def checkrows(board):
    global winner
    if(board[0] == board[1]== board[2] and board[2]!= "-"):
        winner = board[1]
        print(f"Game won and the winner is {board[1]}")
        return gamewon
    if(board[3] == board[4]== board[5] and board[5]!= "-"):
        winner = board[5]
        print(f"Game won and the winner is {board[3]}")
        return gamewon
    if(board[6] == board[7]== board[8] and board[8]!= "-"):
        winner = board[8]
        print(f"Game won and the winner is {board[6]}")
        return gamewon
      
def checkcolumns(board):
    global winner
    if(board[0] == board[3]== board[6] and board[6]!= "-"):
        winner = board[0]
        print(f"Game won and the winner is {board[0]}")
        return gamewon
    if(board[1] == board[4]== board[7] and board[7]!= "-"):
        winner = board[1]
        print(f"Game won and the winner is {board[1]}")
        return gamewon
    if(board[2] == board[5]== board[8] and board[8]!= "-"):
        winner = board[2]
        print(f"Game won and the winner is {board[2]}")  
        return gamewon
      
def checkdiagonal(board):
    global winner
    if(board[0] == board[4]== board[8] and board[8]!= "-"):
        winner = board[0]
        #print(f"Game won and the winner is {board[0]}") 
        return gamewon
    if(board[2] == board[4]== board[6] and board[6]!= "-"):
        winner = board[2]
        print(f"Game won and the winner is {board[2]}") 
        return gamewon

def switchplayer():
    global player
    if (player == "X"):
        player = "O"
    else:
        player = "X"

def checkwin():
    global gameon
    if checkdiagonal(board) or checkrows(board) or checkcolumns(board):
        print(f"the Winner is {winner}")
        gameon = False
        drawboard(board)

while(gameon):
    drawboard(board)
    askuserinput(board)
    checkwin()
    switchplayer()


