
board=["-","-","-",
        "-","-","-",
        "-","-","-"]
def DisplayBoard():
    print(  board[0] + "|" +board[1] + "|" +board[2] 
            + "\n" +board[3] + "|" +board[4] + "|" +board[5]
            + "\n" +board[6] + "|" +board[7] + "|" +board[8])
def SelectPos(player):
    print(player+", Your turn")
    pos=""
    valid=False
    while not valid:
        while pos not in ["1","2","3","4","5","6","7","8","9"]:
            pos=input("Enter  Position between 1-9 only :-")
        pos=int(pos)-1
        if board[pos]=="-":
            valid=True
        else:
            print("Select another position !!")
    print(type(pos))
    board[pos]="X"
    DisplayBoard()

def CheckWin():
    
   pass
   

def Checkemp(pos):
    if board[pos]=="-":
        return True
    else:
        return False
def PlayGame():
    DisplayBoard()
    player="X"
    while True:
        SelectPos(player)

PlayGame()





