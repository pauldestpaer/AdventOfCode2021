lastThree = [0,0,0]
pos = 0
deeper = 0
with open('1\\1_1.txt') as f:
    for line in f.readlines():
        if lastThree[pos] != 0:
            # No need to sum these, if the one being added to the last three is greater than
            # the one being removed, then the sum will be greater
            if int(line) > lastThree[pos]:
                deeper= deeper+1
        # Put ths item onto the array of three previous 
        lastThree[pos] = int(line)
        # Keep position counter in correct place
        pos = pos+1
        if pos == 3:
            pos = 0
print(deeper)