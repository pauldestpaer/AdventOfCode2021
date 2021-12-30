def flashReading(readings, xToCheck, yToCheck):
    # Check each surrounding cell. If its not 0 then increment it else ignore
    keepChecking = False
    for x in range(xToCheck-1, xToCheck+2):
        for y in range(yToCheck-1, yToCheck+2):
            # Don't check points off the grid
            if (x >= 0 and x < len(readings) and
                y >= 0 and y < len(readings[x])):
                if readings[x][y]==0:
                    # already been flashed. Leave alone
                    pass
                else:
                    readings[x][y]+=1

                if readings[x][y]>9:
                    # Reached 9. Will require another run through
                    keepChecking = True
    return keepChecking

readings = []

flashCount = 0

with open('11\\11.txt') as f:
    for line in f.readlines():
        data = line.strip('\n')
        data = list(data)
        for i in range(0, len(data)):
            data[i] = int(data[i])
        readings.append(data)

iterations = 0
notAllFlashed = True
while notAllFlashed:
    flashCount = 0
    iterations += 1
    
    # First - increment each cell. don't record flashes or similar
    for x in range(0, len(readings)):
        for y in range(0, len(readings[x])):
            readings[x][y] +=1 
    
    # Then go over the results looking for flashes and recurse this until no more are found
    keepCheckingThisIteration = True
    while keepCheckingThisIteration:
        keepCheckingThisIteration = False
        for x in range(0, len(readings)):
            for y in range(0, len(readings[x])):
                if readings[x][y] > 9:
                    # flash
                    readings[x][y] = 0
                    flashCount += 1
                    keepChecking = flashReading(readings, x, y)
                    if keepChecking:
                        keepCheckingThisIteration = True # Going to need to go round again

    if flashCount == len(readings)*len(readings[x]):
        break
print(iterations)