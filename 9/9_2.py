def checkValueIs9(readings, xToCheck, yToCheck):
    # Test against an arbitrary location. Handle any missing data (e.g. from
    # being at the edge, or from jagged input arrays) by presuming Lower
    # uuuh..
    # Python suports negative indices and treats those as 'count from the end', so
    # ensure that any -1's passed in are explicitly accepted.
    if int(readings[xToCheck][yToCheck]) == 9:
        return True
    else:
        return False

readings = []

with open('9\\9.txt') as f:
    for line in f.readlines():
        data = line.strip('\n')
        readings.append(list(data))

# Now go over each item in the array and compare it to those above, below, left and 
# right. If lower than all, then add (value+1) to risk score

x = 0
y = 0
basins = []

currentBasin = []
alreadyChecked = []

for x in range (0, len(readings)):
    for y in range(0, len(readings[x])):
        # Is this point a new basin
        if (int(readings[x][y]) < 9 and
           (x,y) not in alreadyChecked):
            # This is part of the current basin. Add it to seed the current basin
            currentBasin.append((x,y))
            foundNew = True
            while foundNew:
                foundNew = False # Presume no new points will be found on this pass
                for point in currentBasin:

                    if point not in alreadyChecked:
                        foundNew = True
                        # Check 4 surrounding points
                        if point[0] > 0:
                            if not checkValueIs9(readings, point[0]-1, point[1]):
                                if (point[0]-1,point[1]) not in currentBasin:
                                    currentBasin.append((point[0]-1,point[1]))
                                    foundNew = True

                        if point[0] < len(readings) - 1:
                            if not checkValueIs9(readings, point[0]+1, point[1]):
                                if (point[0]+1,point[1]) not in currentBasin:
                                    currentBasin.append((point[0]+1,point[1]))
                                    foundNew = True

                        if point[1] > 0:
                            if not checkValueIs9(readings, point[0], point[1]-1):
                                if (point[0],point[1]-1) not in currentBasin:
                                    currentBasin.append((point[0],point[1]-1))
                                    foundNew = True

                        if point[1] < len(readings[x]) - 1:
                            if not checkValueIs9(readings, point[0], point[1]+1):
                                if (point[0],point[1]+1) not in currentBasin:
                                    currentBasin.append((point[0],point[1]+1))
                                    foundNew = True

                        # Add this point to alreadyChecked
                        alreadyChecked.append(point)

            # End while finding new stuff. Therefore the current basin has been measured
            # Store its size, and clear it, but leave already checked so that the same
            # basin isn't accidentally checked again. 
            basins.append(len(currentBasin))     
            currentBasin = [] 
            print(basins)     

basins.sort(reverse=True)
print(basins)
print ((basins[0]*basins[1]*basins[2]))
