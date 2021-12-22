forward = 0
depth = 0
with open('2_1.txt') as f:
    for line in f.readlines():
        # split the line to get the direction and the amount
        details = line.split(' ')
        if details[0] == 'forward':
            forward += int(details[1])
        if details[0] == 'down':
            depth += int(details[1])
        if details[0] == 'up':
            depth -= int(details[1])
print(forward*depth)
        