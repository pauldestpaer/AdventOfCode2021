
start = []
end = []
covered = []
hitTwice = []
startLine = ''
endLine = ''
totalHitTwice = 0
with open('5\\5.txt') as f:
    for line in f.readlines():
        # Each line is (2 coords) -> (2 coords). 
        # Get this data into start,finish gruops.
        splitLine = line.strip('\n').split('->')
        startLine = splitLine[0].strip(' ').split(',')
        start.append([int(startLine[0]), int(startLine[1])])
        endLine = splitLine[1].strip(' ').split(',')
        end.append([int(endLine[0]), int(endLine[1])])

print(start[0])
print(end[0])

# Pick each set where either the x or y coords match, then write all
# the coords covered into a single grid with a count being incremented
lower = 0
higher = 0
stepx = 0
stepy = 0
startx = 0
starty = 0
endx = 0
endy = 0
length = 0
for pos in range(len(start)):
    print(pos)
    if start[pos][0] == end[pos][0]:
        # x coords match, so note coverage, and note recoverage if necessary
        if start[pos][1] > end[pos][1]:
            lower = end[pos][1]
            higher = start[pos][1]
        else:
            higher = end[pos][1]
            lower = start[pos][1]

        for y in range(lower, higher + 1): # Needs to include the higher value
            if [start[pos][0], y] not in covered:
                covered.append([start[pos][0], y])
                continue
            elif [start[pos][0], y] not in hitTwice:
                hitTwice.append([start[pos][0], y])
                totalHitTwice += 1 # First instance of a duplicate on this point
                continue
            else: # its a repetition of hitTwice. Do nothing
                pass
    
    elif start[pos][1] == end[pos][1]:
        # y coords match, so note coverage, and note recoverage if necessary
        if start[pos][0] > end[pos][0]:
            lower = end[pos][0]
            higher = start[pos][0]
        else:
            higher = end[pos][0]
            lower = start[pos][0]

        for x in range(lower, higher + 1): # Needs to include the higher value
            if [x, start[pos][1]] not in covered:
                covered.append([x, start[pos][1]])
                continue
            elif [x, start[pos][1]] not in hitTwice:
                hitTwice.append([x, start[pos][1]])
                totalHitTwice += 1 # First instance of a duplicate on this point
                continue
            else: # its a repetition of hitTwice. Do nothing
                pass

    else:
        # neither match
        if start[pos][0] > end[pos][0]:
            stepx = -1
            endx = end[pos][0] - 1
        else:
            stepx = 1
            endx = end[pos][0] + 1

        if start[pos][1] > end[pos][1]:
            stepy = -1
            endy = end[pos][1] - 1
        else:
            stepy = 1
            endy = end[pos][1] + 1

        length = abs(start[pos][0] - end[pos][0]) + 1

        for offset in range(0, length): # Needs to include the higher value
            if [start[pos][0] + (offset*stepx), start[pos][1] + (offset*stepy)] not in covered:
                covered.append([start[pos][0] + (offset*stepx), start[pos][1] + (offset*stepy)])
                continue
            elif [start[pos][0] + (offset*stepx), start[pos][1] + (offset*stepy)] not in hitTwice:
                hitTwice.append([start[pos][0] + (offset*stepx), start[pos][1] + (offset*stepy)])
                totalHitTwice += 1 # First instance of a duplicate on this point
                continue
            else: # its a repetition of hitTwice. Do nothing
                pass

print(totalHitTwice)