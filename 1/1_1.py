previous = 0
deeper = 0
with open('1\\1_1.txt') as f:
    for line in f.readlines():
        if previous != 0:
            if int(line) > previous:
                deeper= deeper+1
        previous = int(line)
print(deeper)