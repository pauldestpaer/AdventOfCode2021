class Done( Exception ):
    # dummy exception class to allow for break all syntax
    pass

numbers = []
lineOnBoard = []
board = []
boards = []
with open('4\\4.txt') as f:
    for line in f.readlines():
        if len(numbers) == 0:
            # first line. Its the draw numbers
            numbers = line.strip('\n').split(',')
        elif line != '\n':
            # add line to board. Clear out excess spaces so each number is seperated by just one space
            lineOnBoard = line.strip().replace('  ', ' ').strip('\n').split(' ')
            board.append(lineOnBoard)
        else:
            # Its an empty string. Add the completed board to the boards list
            # and clear it ready for the next board
            if len(board) > 0:
                boards.append(board)
                board = []
    # End of file. append the last board
    boards.append(board)

# All loaded up. now, for each number drawn, test each board to see
# if either a whole lineOnBoard is matched or if a specific array position
# is matched in all 5 lines. 
drawnNumbers = []
chosenBoard = None
lastNumber = 0
try:
    for number in numbers:
        lastNumber = number # Will need this later
        # add to the draw
        drawnNumbers.append(int(number))
        for board in boards:
            # Test each line
            for lineOnBoard in board:
                got =True
                for pos in range(len(lineOnBoard)):
                    if int(lineOnBoard[pos]) not in drawnNumbers:
                        got = False
                        break # no need for further checks
                if got:
                    chosenBoard = board
                    raise Done

            # Test each position
            for pos in range(5):
                got = True
                for lineOnBoard in board:
                    if int(lineOnBoard[pos]) not in drawnNumbers:
                        got = False
                        break # no need for further checks
                if got:
                    chosenBoard = board
                    raise Done
except Done:
    pass # Using this a break all as py is shit.

print(chosenBoard)
print(drawnNumbers)

# Now identify the unselected numbers from the selected board and 
# multiply them by the last number selected
sumOfUnselected = 0
for lineOnBoard in chosenBoard:
    for pos in range(len(lineOnBoard)):
        if int(lineOnBoard[pos]) not in drawnNumbers: 
            sumOfUnselected += int(lineOnBoard[pos])

print (int(sumOfUnselected)*int(lastNumber))