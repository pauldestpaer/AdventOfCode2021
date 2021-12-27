def matchLetterToSection(clue):
    # Examine the 10 strings in the clue to determine which letter matches which part
    # of a standard 7 bar digital digit display.
    map = {}
    twoLetters = ()
    threeLetters = ()
    fourLetters = ()
    fiveLetters = []
    sixLetters = []
    sevenLetters = ()
    # Rule 1 - Map off the 1, 7, 4 and 8, and group the rest.
    for item in clue:
        if len(item) == 2:
            map['1'] = item
        if len(item) == 3:
            map['7'] = item
        if len(item) == 4:
            map['4'] = item
        if len(item) == 5:
            fiveLetters.append(set(item))
        if len(item) == 6:
            sixLetters.append(set(item))
        if len(item) == 7:
            map['8'] = item
    
    # rule 2 - If it has 6 chars and only one not matching in 3 and 4, then the item
    # is a '9'
    theFour = set(map['4'])
    theSeven = set(map['7'])
    for item in sixLetters:
        remaining = item.difference(theFour).difference(theSeven)
        if len(remaining) == 1:
            map['9'] = ''.join(item)
            sixLetters.remove(item)
            break
    
    # rule 3 - If 5 chars and only 2 match the 4 its a '2'
    for item in fiveLetters:
        remaining = item.difference(theFour)
        if len(remaining) == 3:
            map['2'] = ''.join(item)
            fiveLetters.remove(item)
            break

    # Rule 4 - If 5 chars and all 3 are in the 7 its a '3'
    for item in fiveLetters:
        remaining = item.difference(theSeven)
        if len(remaining) == 2:
            map['3'] = ''.join(item)
            fiveLetters.remove(item)
            break
        
    # Therefore remaining item in the 5 char set is the '5'
    map['5'] = ''.join(fiveLetters[0])

    # Finally, if 6 chars and only misses the '5' by one its the '6'
    theFive = set(map['5'])
    for item in sixLetters:
        remaining = item.difference(theFive)
        if len(remaining) == 1:
            map['6'] = ''.join(item)
            sixLetters.remove(item)
            break

    # Leaving the '0'
    map['0'] = ''.join(sixLetters[0])

    for k, v in map.items():
        map[k] = set(v)

    return map

def identifyDigit(digit, map):
    # Test supplied digit by setting it and setwise comparing it to 
    digitAsSet = set(digit)
    for key, value in map.items():
        if len(digitAsSet.difference(value)) == 0 and len(value.difference(digitAsSet)) == 0:
            return key

total = 0   # Sums up the numbers of 1,4,7,8 that appear
toMatch = ['1','4','7','8']
with open('8\\8.txt') as f:
    for line in f.readlines():
        clue = line.split('|')[0].strip(' ')
        clue = clue.split(' ')
        digits = line.split('|')[1].strip('\n').strip(' ')
        digits = digits.split(' ')

        map = matchLetterToSection(clue)
        # Now using the map, identify each digit
        outputAsString = ''
        for item in digits:
            digit = identifyDigit(item, map)
            outputAsString = outputAsString + digit

        total += int(outputAsString)

print(total)
