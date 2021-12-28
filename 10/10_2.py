lines = []

with open('10\\10.txt') as f:
    for line in f.readlines():
        data = line.strip('\n')
        lines.append(data)

# Check each line for evidence of corruption
autoCompleteScores = []
autoCompleteScore = 0
for line in lines:
    chars = []
    autoCompleteScore = 0
    corrupt = False
    for char in line:
        if char in ['{', '<', '(', '[']:
            # add on
            chars.append(char)
        else:
            # pop off and check
            matchingChar = chars.pop()
            if (matchingChar=='{' and char != '}' or
                matchingChar=='<' and char != '>' or
                matchingChar=='(' and char != ')' or
                matchingChar=='[' and char != ']'):
                # Corrupt line found, so..
                corrupt = True
                break
    
    # Line is incomplete, so process the missing characters as per the puzzle rules
    if not corrupt and len(chars) > 0:
        while len(chars) > 0:
            # First multiply by 5
            autoCompleteScore *= 5
            # then add a value based upon the popped char
            matchingChar = chars.pop()
            if matchingChar=='(':
                autoCompleteScore+=1
            if matchingChar=='[':
                autoCompleteScore+=2
            if matchingChar=='{':
                autoCompleteScore+=3
            if matchingChar=='<':
                autoCompleteScore+=4

        autoCompleteScores.append(autoCompleteScore)

# finally, sort the scores and pick the middle one. Puzzle has guaranteed an odd number
autoCompleteScores.sort()
print(autoCompleteScores[int((len(autoCompleteScores)-1)/2)])