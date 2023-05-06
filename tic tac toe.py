import random
board=['-','-','-',
       '-','-','-',
       '-','-','-']
currentplayer='X'
winner=None
gamerunning=True

def printboard(board):
    print(board[0]+'|'+board[1]+'|'+board[2])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[6]+'|'+board[7]+'|'+board[8])
printboard(board)

def playerinput(board):
    inp=int(input('enter a number 1-9:'))
    if inp>=1 and inp<=9 and board[inp-1]=='-':
        board[inp-1]=currentplayer
    else:
        print('oops player is already in that spot!')

def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!='-':
        winner=board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!='-':
        winner=board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!='-':
        winner=board[6]
        return True

def checkvertical(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!='-':
        winner=board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!='-':
        winner=board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!='-':
        winner=board[2]
        return True

def checkdiagonal(board):
     global winner
     if board[0]==board[4]==board[8] and board[0]!='-':
        winner=board[0]
        return True
     elif board[2]==board[4]==board[6] and board[2]!='-':
        winner=board[2]
        return True

def checktie(board):
    if '-' not in board:
        printboard(board)
        print("it's a tie")
        gamerunning=False

def checkwin():
    if checkdiagonal(board) or checkvertical(board) or checkhorizontal(board):
        return f'the winner is {winner}'

def switchplayer():
    global currentplayer
    if currentplayer=='X':
        currentplayer='O'
    else:
        currentplayer='X'

def computer(board):
    while currentplayer=='O':
        position=random.randint(0,8)
        if board[position]=='-':
            board[position]='O'
            switchplayer()

        
while gamerunning:
    printboard(board)
    playerinput(board)
    #checkwin()
    #checktie(board)
    switchplayer()
    computer(board)
    if type(checkwin())==str:
        print(checkwin())
        break
    checktie(board)
    
    

    
