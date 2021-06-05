# Tic Tac Toe Project

# TODO:
# - create AI to play with?
#

# prints out a board state list
def printBoard(boardStateList):
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
        userInput = input(f'Player {playerChar} please input position number: ')

        # check if input is digit
        if not userInput.isdigit():
            print("Input is not a digit, please try again")
            continue

        # check if within range
        if not int(userInput) in range(1,10):
            print("Input is outside of range, please select between 1-9")
            continue

        # check if value has not been used already
        valueTryingToReplace = convertPositionIntToTuple(int(userInput))
        if (boardStateList[valueTryingToReplace[0]][valueTryingToReplace[1]]) in ('X', 'O'):
            print("Position has already been used, please select a different spot")
            continue

        currentlyInvalidInput = False

    return int(userInput)


# converts the int form of user input into a tuple that can be used for 2D list
def convertPositionIntToTuple(positionInInt):
    positionDictionary = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                          4: (1, 0), 5: (1, 1), 6: (1, 2),
                          7: (2, 0), 8: (2, 1), 9: (2, 2)}
    return positionDictionary[positionInInt]


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

    # check diagonal
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
currBoard = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
printBoard(currBoard)

noWinnerExists = True
turnCounter = 0
currPlayer = 'O'

# keep looping until a winner is found
while noWinnerExists:
    # alternate current player
    currPlayer = 'X' if currPlayer == 'O' else 'O'

    # get user input and alter board accordingly
    currUserInput = getUserInput(currBoard, currPlayer)  # get input
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

if currPlayer is not None:
    print(f'The winner is {currPlayer}')
else:
    print('There is a draw')
