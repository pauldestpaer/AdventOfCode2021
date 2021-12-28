def checkValueIsLower(readings, value, xToCheck, yToCheck):
    # Test against an arbitrary location. Handle any missing data (e.g. from
    # being at the edge, or from jagged input arrays) by presuming Lower
    # uuuh..
    # Python suports negative indices and treats those as 'count from the end', so
    # ensure that any -1's passed in are explicitly accepted.
    if xToCheck < 0 or yToCheck < 0:
        return True
    try:
        if value < readings[xToCheck][yToCheck]:
            return True
    except IndexError as e:
        return True
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
totalRisk = 0

for x in range (0, len(readings)):
    for y in range(0, len(readings[x])):
        if (checkValueIsLower(readings, readings[x][y], x-1, y) and
        checkValueIsLower(readings, readings[x][y],  x+1,  y) and
        checkValueIsLower(readings, readings[x][y], x,  y-1) and
        checkValueIsLower(readings, readings[x][y],  x,  y+1)):
        # Its lower, so..
            totalRisk = totalRisk + int(readings[x][y]) + 1

print (totalRisk)


