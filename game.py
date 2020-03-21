import random

# gloabl variables
inst = '''Welcome to the game, here are the instructions how to play.
You will be playing aganist computer (dumb computer, you will win don't worry).
    X -> already played by user,
    Y -> already played by computer,
    _ -> empty.
You will have select unselected position to mark according to the below diagram.
  1 | 2 | 3 |
 ------------
  4 | 5 | 6 |
 ------------
  7 | 8 | 9 |

 All the best......'''
print(inst)

# current state of the game
state = {1 : "_", 2 : "_", 3 : "_", 4 : "_", 5 : "_", 6 : "_", 7 : "_", 8 : "_", 9 : "_" }

# wining cordinates
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# checks for draw math, last time when i created an andriod app for this game i forgot to put this part
def isDraw():
    flageD = True
    for i in range(1,10):
        if state[i] == "_":
            flageD = False
    if(flageD):
        print("Draw match... :|")
        exit()


# provides idea of how the game looks like
def userOutput():
    num = 1
    for i in range(1,4):
        for i in range(1,4):
            print(" "+state[num]+" | ", end = '')
            num += 1
        print()
        print("--------------")

# brains of game and changes state of the position
def logic():
    inp = 10



# User player
def userInput():
    print("User's turn")
    pos = input("Enter the position number as per the instructions above: ")
    if !pos >=1 && pos <=9:
        print("Enter numbers between 1-9")
        userInput()
    if state[int(pos)] != "_":
        print("choose already, try again..")
        userInput()
    else:
        state[int(pos)] = "X"

# system player
def sysInput():
    pos = random.randint(1,9)
    if state[int(pos)] != "_":
        sysInput()
    else:
        state[int(pos)] = "Y"

#check if anyone has won
def logic():
    flagX = False
    flagY = False
    # print("usr")
    for occ in win:
        flagX = True
        for i in occ:
            if state[int(i)] == "X":
                # print("in X-T")
                pawn =10
            else:
                # print("in X-F")
                flagX = False
        if(flagX):
            print("User wins :)")
            exit()
        if(flagY):
            print("System wins :(")
            exit()
    # print("sys")
    for occ in win:
        flagY = True
        for i in occ:
            if(state[int(i)] == "Y"):
                # print("in Y-T")
                pawn = 10
            else:
                # print("in X-F")
                flagY = False
        if(flagX):
            print("User wins :)")
            exit()
        if(flagY):
            print("System wins :(")
            exit()
    isDraw();

def main():
    while(True):
        userInput()
        userOutput()
        logic()
        print("System's turn")
        sysInput()
        userOutput()
        logic()


main()
