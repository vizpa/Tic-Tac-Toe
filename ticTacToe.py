import random

# randomly picks player or cpu's turn
turn = (random.randrange(1, 3))

num = 1
game = True
tup = range(1, 10)
# unpack tup values
a1, a2, a3, a4, a5, a6, a7, a8, a9 = tup

# possible winning combinations
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
    [1, 4, 7], [2, 5, 8], [3, 6, 9],
    [1, 5, 9], [3, 5, 7]]

playerMe = "O"
playerCPU = "X"

chance2win = 0
canWinCPU = []
canWinUser = []

dispB = True


def DisplayBoard(board):
    #
    # the function accepts one parameter containing the board's current
    # status and prints it out to the console
    #
    # prints +-------+...
    def line1():
        [print("+", "-" * 7, sep="", end="") for i in range(3)]
        print("+")
    # prints |       |...
    def line2():
        [print("|", " " * 7, sep="", end="") for i in range(3)]
        print("|")
    # prints Field's number, 'X' or 'O'
    for _ in range(3):
        line1()
        line2()
        for _ in range(3):
            global num
            global field
            field = str(num)
            print("|", " " * 3, globals()
                  ["a" + field], " " * 3, sep="", end="")
            num += 1
        print("|")
        line2()
    line1()
    num = 1


def EnterMove(board):
    #
    # the function accepts the board current status, asks the user about their move,
    # checks the input and updates the board according to the user's decision
    #
    global playerMe  # 'X' or 'O'
    global canWinUser
    global dispB
    while True:
        try:
            move = input('Enter your move: ')
            if 1 <= int(move) < 10:
                if globals()["a" + move] != "O" and globals()["a" + move] != "X":
                    # updates variable to 'X' or 'O'
                    globals()["a" + move] = playerMe
                    canWinUser.append(int(move))
                    return
                else:
                    # checks if Field is free to play
                    print("TRY AGAIN: ", end="")
            else:
                print("Sorry, ", move, "is not on the board!")
        except ValueError:
            print("Sorry, ", move, "is not on the board!")

def MakeListOfFreeFields(board):
    #
    # the function browses the board and builds a list of all the free squares;
    # the list consists of tuples, and each tuple is a pair of row and column numbers
    #
    # checks if game is over (False)
    global game
    freeField = []
    for i in tup:
        if globals()["a" + str(i)] != "O" and globals()["a" + str(i)] != "X":
            freeField.append(i)
    if len(freeField) == 0:
        game = False


def VictoryFor(board, sign):
    #
    # the function analyzes the board status in order to check if
    # the player using 'O's or 'X's has won the game
    #
    global game
    global win
    markedFields = []
    for i in tup:
        if globals()["a" + str(i)] == sign:
            markedFields.append(i)
    for numList in win:
        # compares markedFields to possible winninc comb. (win)
        if numList[0] in markedFields and numList[1] in markedFields and \
                numList[2] in markedFields:
            if sign == playerMe:
                print('You have won!!')
            else:
                print("Sorry, you lost.")
            game = False
    markedFields = []


def DrawMove(board):
    #
    # the function draws the computer's move and updates the board
    #
    global playerCPU
    global win
    global chance2win
    global game
    global compMove
    global canWinUser
    global canWinCPU
    global dispB
    print("CPU's turn: ", end="")
    # CPU takes empty field
    def winMove(numList):   
        for i in numList:
            if globals()["a" + str(i)] != playerMe and \
                globals()["a" + str(i)] != playerCPU:
                globals()["a" + str(i)] = playerCPU
                canWinCPU.append(int(i))
                print(i)
                return
    # compare possible winning comb. (win) vs CPU and user's fields           
    chance2win = 0
    for numList in win:
        for element in numList:
            if element in canWinCPU:
                chance2win += 1
            if element in canWinUser:
                chance2win -= 1
        # if CPU can win, play to win
        if chance2win == 2:
            winMove(numList)
            return
        # if user can win, play not to lose
        if chance2win == -2:
            winMove(numList)
            return
        chance2win = 0
    # if there isn't a chances to win, find empty fields to play
    compMoveLst = range(1, 10)
    compMoveLst = list(set(compMoveLst) - set(canWinCPU))
    compMoveLst = list(set(compMoveLst) - set(canWinUser))
    compMove = str(random.choice(compMoveLst))
    globals()["a" + compMove] = playerCPU
    canWinCPU.append(int(compMove))
    print(compMove)
    return

def main():
    global game
    global turn
    global playerMe
    global playerCPU
    global tup
    global dispB
    global canWinUser
    global canWinCPU
    # Let player select 'X' or 'O'
    print("\nNoughts and Crosses,\nSelect which one you want to be")
    while True:
        try:
            playerMe = input('"X" or "O": ').upper()
            if playerMe == "X":
                playerCPU = "O"
                break
            elif playerMe == "O":
                playerCPU = "X"
                break
            else:
                print("Sorry, the only options were Os and Xs\n" +
                      "You are X!")
                playerMe = "X"
                playerCPU = "O"
        except ValueError:
            print("Sorry, the only options are Os and Xs")

        break
    # if user goes 1st, display empty board
    if turn == 1:
        DisplayBoard(game)
    # play!!
    while game:
        if turn == 1:
            EnterMove(game)
            turn = 2
        else:
            DrawMove(game)
            turn = 1
        DisplayBoard(game)
        VictoryFor(game, "O")
        VictoryFor(game, "X")
        MakeListOfFreeFields(game)
    else:
        print("GAME OVER")
        # play again?
        while True:
            try:
                playAgn = input(
                    'Do you want to keep playing?\n"Y" or "N": ').upper()
                if playAgn == "Y":
                    for i in tup:
                        globals()["a" + str(i)] = tup[i-1]
                    canWinUser = []
                    canWinCPU = []
                    game = True
                    main()
                elif playAgn == "N":
                    print("Party easy, drive safe,\n" +
                          "   and return with a smile on your face!\n")
                    exit()
                else:
                    print("Sorry,", playAgn, "is not an option")
            except ValueError:
                print("Sorry,", playAgn, "is not an option")


if __name__ == "__main__":
    main()
