def distance(moveTo, positions):
    distance = 0
    for crab in positions:
        distance += abs(moveTo - crab)
    return distance

positions = []
maxPosition = 0
with open('7\\7.txt') as f:
    for line in f.readlines():
        # just one line to read here. Split it by ','...
        for crab in line.split(','):
            positions.append(int(crab))
            #if int(crab) > maxPosition:
            #    maxPosition = int(crab)

# Get the average of positions, and the nearest common position

test = round(max(positions)/2)
moveBy = test
bestDistance = distance(test, positions)
moveUp = 0
moveDown = 0

done = False
while not done:
    # Iterate through numbers by halving gaps each time to find the optimal position to go to
    moveBy = round(moveBy/2)
    if moveBy < 1:
        moveBy = 1 # in case of rounding silliness

    moveUp = round(test + moveBy)
    newdistance = distance(moveUp, positions)
    if newdistance < bestDistance:
        # Beaten previous best
        bestDistance = newdistance
        test = moveUp
        continue

    moveDown = round(test - moveBy)
    newdistance = distance(moveDown, positions)
    if newdistance < bestDistance:
        # Beaten previous best
        bestDistance = newdistance
        test = moveDown
        continue
 
    # Neither success condition was hit.
    if moveBy == 1:
        break

print(test)
print(bestDistance)
