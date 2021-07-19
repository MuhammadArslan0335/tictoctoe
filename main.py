# make lists for player 1 & player 2 in which the numbers will be saved
histP1 = []
histP2 = []

# make a master list in which the history of player 1 & 2 will be appended
mastrH = []
mastrH.append(histP1)
mastrH.append(histP2)

# the sequence of wining board
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]

# select to play with computer or multiplayer

slcttyp = input("""Enter "M" to play with another Player: """)

if slcttyp == "M" or slcttyp =="m":
    print("You are playing against another player!")

print("\nHere is your Board!")
def gameboard():
    n = 0
    for i in range (1, 4):
        for j in range (1, 4):
            print(n + 1, end= ' ')
            n = n +1
        print()
def moveplayer1():
    moveP1 = int(input("Player 1: Please enter the number at where you want to place your symbol: "))
    histP1.append(moveP1)
def moveplace():
    countr = 0
    for i in range (1, 4):
        for j in range (1, 4):
            countr = countr + 1
            if countr in mastrH[0]:
                print(symbP1, end=' ')
            elif countr in mastrH[1]:
                print(symbP2, end= ' ')
            else:
                print("-", end=' ')
        print()
def moveplayer2():
    moveP2 = int(input("Player 2: Please enter the number at where you want to place your symbol: "))
    histP2.append(moveP2)


def checkfun():
    check1 = all(item in mastrH[0] for item in win)
    if check1 is True and len(mastrH[0]) >= 3:
        print("Winner")
        print("Game Over!")

    check2 = all(item in mastrH[1] for item in win)
    if check2 is True and len(mastrH[1]) >= 3:
        print("Player 2 Winner!")
        print("Game Over!")
    #
    # if len(mastrH[0]) + len(mastrH[1]) == 9:
    #     print("Game Tie!")

if slcttyp == "M" or slcttyp == "m":
    gameboard()
    symbP1 = input("""Player 1: Select your symbol "#" or "$": """)
    if symbP1 == "#":
        print("Player 1: Your symbol for the game is: #")
    else:
        print("Player 1: Your symbol for the game is: $")
    symbP2 = input("""Player 2: Select your symbol "#" or "$": """)
    print("Player 2: Your symbol for the game is: ", symbP2)
    while symbP2 == symbP1:
        symbP2 = input("""Select another symbol: """)
        if symbP2 == symbP1:
            print("Your Symbol is: ", symbP2)
    moveplayer1()
    moveplace()
    moveplayer2()
    moveplace()
    checkfun()
    check = False

    while len(mastrH[0]) + len(mastrH[1]) < 9:
        moveplayer1()
        moveplace()
        for i in range(len(win)):
            check1 = all(item in mastrH[0] for item in win[i])
            if check1 is True and len(mastrH[0]) >= 3:
                print("Player 1 Winner")
                print("Game Over!")
                check = True
                break
            if len(mastrH[0]) + len(mastrH[1]) == 9:
                print("Game Tie!")
                check = True
                break
        if check == True:
            break
        moveplayer2()
        moveplace()
        for i in range(len(win)):
            check2 = all(item in mastrH[1] for item in win[i])
            if check2 is True and len(mastrH[1]) >= 3:
                print("Player 2 Winner!")
                print("Game Over!")
                check = True
                break
            if len(mastrH[0]) + len(mastrH[1]) == 9:
                print("Game Tie!")
                check = True
                break
        if check == True:
            break
