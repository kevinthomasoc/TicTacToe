import random
#Declare Variables
board = [1,2,3,4,5,6,7,8,9]    

#Player Moves
def xmove():
    while True:
        tile = int(input("What tile would you like to place your letter in?"))

        indexx = tile - 1
        if (board[indexx] == 'X') or (board[indexx] == 'O'):
            print("A player has already moved there. Please choose a different slot")
            continue
        else:
            
            board[indexx] = 'X'

                
            print(board[0], '|', board[1], '|', board[2])
            print('---------')
            print(board[3], '|', board[4], '|', board[5])
            print('---------')
            print(board[6], '|', board[7], '|', board[8])
            print("                                     ")
            print("                                     ")
            print("                                     ")
            break
def omove():
    while True:
        tile = int(input("What tile would you like to place your letter in?"))

        indexx = tile - 1
        if (board[indexx] == 'X') or (board[indexx] == 'O'):
            print("A player has already moved there. Please choose a different slot")
            continue
        else:
            
            board[indexx] = 'O'

                
            print(board[0], '|', board[1], '|', board[2])
            print('---------')
            print(board[3], '|', board[4], '|', board[5])
            print('---------')
            print(board[6], '|', board[7], '|', board[8])
            print("                                     ")
            print("                                     ")
            print("                                     ")
            break
def pcMove():
    while True:
        randominteger = random.choice(board)
        integer = isinstance(randominteger, int)
        if integer == True:
            pcindex = randominteger - 1
            board[pcindex] = "X"
            print(board[0], '|', board[1], '|', board[2])
            print('---------')
            print(board[3], '|', board[4], '|', board[5])
            print('---------')
            print(board[6], '|', board[7], '|', board[8])
            print("                                     ")
            print("                                     ")
            print("                                     ")
            break
            
        else:
            continue

#Check for wins
def winCheck():
    #Horizontal Check
    if (board[0] == board[1]) and (board[1] == board[2]):
        return("PLAYER " + board[0] + " WINS!!")
    if (board[3] == board[4]) and (board[4] == board[5]):
        return("PLAYER " + board[3] + " WINS!!")
    if (board[6] == board[7]) and (board[7] == board[8]):
        return("PLAYER " + board[6] + " WINS!!")
    #Vertical Check
    if (board[0] == board[3]) and (board[3] == board[6]):
        return("PLAYER " + board[0] + " WINS!!")
    if (board[1] == board[4]) and (board[4] == board[7]):
        return("PLAYER " + board[1] + " WINS!!")
    if (board[2] == board[5]) and (board[5] == board[8]):
        return("PLAYER " + board[2] + " WINS!!")
    #Diagonal Check
    if (board[0] == board[4]) and (board[4] == board[8]):
        return("PLAYER " + board[0] + " WINS!!")
    if (board[2] == board[4]) and (board[4] == board[6]):
        return("PLAYER " + board[2] + " WINS!!")

#Check for Draw
def drawCheck():
    for char in board:
        x = isinstance(char, int)
        if x == True:
            return True
        


#Multiplayer Game Function
def multiPlayer():
    move = 0
    while True:
#Calculate what player is moving

        if ord(playerone) == (79) or ord(playerone) == (111):
            if move % 2 == 0:
                omove()
            elif move % 2 != 0:
                xmove()
            
        elif ord(playerone) == (88) or ord(playerone) == (120):
            
            if move % 2 == 0:
                xmove()
            elif move % 2 != 0:
                omove()

        if drawCheck() != True:
            print("The game is a draw!")
            break


        if winCheck() != None:
            print(winCheck())
            break
            
        move = move + 1

#Singleplayer Game Function 
def singlePlayer():
    move = 0
    while True:
        if move % 2 == 0:
            omove()
        elif move % 2 != 0:
            pcMove()
        
    
        if drawCheck() != True:
            print("The game is a draw!")
            break


        if winCheck() != None:
            print(winCheck())
            break
            
        move = move + 1

#Single or Multiplayer
player = input("1. Single Player\n2. Multiplayer\nEnter either 1 or 2")

if player != "1":
    #Player Select
    while True:
        playerone = input("Player one, do you want to be X or O?")
        if ord(playerone) == (79) or ord(playerone) == (111):
            playerone = "O"
            print("You will be player O")
            playertwo = "X"
            print("Player two, you will be X")
            break
        elif ord(playerone) == (88) or ord(playerone) == (120):
            playerone = "X"
            print("You will be player X")
            playertwo = "O"
            print("Player two, you will be O")
            break
        else:
            print("Please enter either O or X")
            continue
        break

#Multiplayer Game
if player != "1":
    #Print Initial Board
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
    multiPlayer()
#Singleplayer Game
if player == "1":
    #Print Initial Board
    print(board[0], '|', board[1], '|', board[2])
    print('---------')
    print(board[3], '|', board[4], '|', board[5])
    print('---------')
    print(board[6], '|', board[7], '|', board[8])
    singlePlayer()


      
    
    










    
    
    

        

