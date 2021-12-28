lines = []

with open('10\\10.txt') as f:
    for line in f.readlines():
        data = line.strip('\n')
        lines.append(data)

# Check each line for evidence of corruption
corruptScore = 0

for line in lines:
    chars = []
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
                if char==')':
                   corruptScore+=3
                if char==']':
                   corruptScore+=57
                if char=='}':
                   corruptScore+=1197
                if char=='>':
                   corruptScore+=25137

print(corruptScore)