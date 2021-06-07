# Tic Tac Toe Project
# Choose the number of players to play Tic Tac Toe

import random


# get input to see the number of players
def determineNumPlayers():
    currentlyInvalidInput = True

    while currentlyInvalidInput:
        userInput = input(f'Enter the number of players (1-2): ')

        # check if input is digit
        if not userInput.isdigit():
            print("Input is not a digit, please try again")
            continue

        # check if within range
        if not int(userInput) in range(1, 3):
            print("Input is outside of range, please select between 1-2")
            continue

        currentlyInvalidInput = False

    return int(userInput)


# prints out a board state list
def printBoard(boardStateList):
    print("\n")
    for i in range(len(boardStateList)):
        for j in range(len(boardStateList[i])):

            if j < len(boardStateList[i]) - 1:  # don't include final | at end of row
                print(boardStateList[i][j], end=' | ')
            else:
                print(boardStateList[i][j], end='\n')

        print('-' * (len(boardStateList[i] * 3)))  # add '-' triple that of elements per row


# gets and validates user input
def getUserInput(boardStateList, playerChar):
    currentlyInvalidInput = True

    while currentlyInvalidInput:
        userInput = input(f'Player {playerChar} please input position number (1-9): ')

        # check if input is digit
        if not userInput.isdigit():
            print("Input is not a digit, please try again")
            continue

        # check if within range
        if not int(userInput) in range(1, 10):
            print("Input is outside of range, please select between 1-9")
            continue

        # check if value has not been used already
        valueTryingToReplace = convertPositionIntToTuple(int(userInput))
        if (boardStateList[valueTryingToReplace[0]][valueTryingToReplace[1]]) in ('X', 'O'):
            print("Position has already been used, please select a different spot")
            continue

        currentlyInvalidInput = False

    return int(userInput)


# see if user wants to continue playing the game
def determineIfWantToCont():
    while True:
        userInput = input(f'Do you want to continue? (Y/N): ')

        # check if input is digit
        if userInput == 'Y':
            return True
        elif userInput == 'N':
            return False
        else:
            print("Please enter either Y or N: ")
            continue


# computer will randomly choose if there is only one player
def AIChooses(boardStateList):
    # find all available spots
    listOfAvailable = []
    counter = 0
    for i in range(0, len(boardStateList)):
        for j in range(0, len(boardStateList[0])):
            counter += 1

            # include into list if spot is not taken
            if boardStateList[i][j].isdigit():
                listOfAvailable.append(counter)

    # choose one of the available spots
    return random.choice(listOfAvailable)


# converts the int form of user input into a tuple that can be used for 2D list
def convertPositionIntToTuple(positionInInt):
    positionDictionary = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 9: (2, 2)}
    return positionDictionary[positionInInt]


# check if there is a winner
def checkForWinner(boardStateList, alteredPosition, currPlayer):
    # check curr row
    if ((boardStateList[alteredPosition[0]][0] == currPlayer) and
            (boardStateList[alteredPosition[0]][1] == currPlayer) and
            (boardStateList[alteredPosition[0]][2] == currPlayer)):
        return True

    # check curr column
    if ((boardStateList[0][alteredPosition[1]] == currPlayer) and
            (boardStateList[1][alteredPosition[1]] == currPlayer) and
            (boardStateList[2][alteredPosition[1]] == currPlayer)):
        return True

    # check both diagonals
    if ((boardStateList[0][0] == currPlayer) and
            (boardStateList[1][1] == currPlayer) and
            (boardStateList[2][2] == currPlayer)):
        return True

    if ((boardStateList[2][0] == currPlayer) and
            (boardStateList[1][1] == currPlayer) and
            (boardStateList[0][2] == currPlayer)):
        return True

    return False


# main
keepPlaying = True

while keepPlaying:

    # initial values
    currBoard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    noWinnerExists = True
    turnCounter = 0
    currPlayer = 'O'

    numPlayers = determineNumPlayers()
    printBoard(currBoard)

    # keep looping until a winner is found
    while noWinnerExists:
        # alternate current player
        currPlayer = 'X' if currPlayer == 'O' else 'O'

        # get user input and alter board accordingly
        if currPlayer == 'X' and numPlayers == 1:  # if only one player
            currUserInput = getUserInput(currBoard, currPlayer)
        else:
            currUserInput = AIChooses(currBoard)
            print(f"Player O has chosen {currUserInput}")

        alteredPosition = convertPositionIntToTuple(currUserInput)  # convert input
        currBoard[alteredPosition[0]][alteredPosition[1]] = currPlayer  # apply input
        printBoard(currBoard)  # print

        # check for winner
        noWinnerExists = not checkForWinner(currBoard, alteredPosition, currPlayer)

        # break if there is a tie
        turnCounter += 1
        if turnCounter >= 9:
            currPlayer = None
            break

    # print winner
    if currPlayer is not None:
        print(f'The winner is {currPlayer}')
    else:
        print('There is a draw')

    # see if user wants to continue playing
    keepPlaying = determineIfWantToCont()
