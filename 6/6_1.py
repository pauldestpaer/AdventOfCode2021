fishes = []
with open('6.txt') as f:
    for line in f.readlines():
        # just one line to read here. Split it by ','...
        splitLine = line.split(',')
        # And feed it into the array
        for item in splitLine:
            fishes.append(int(item))

# Now, loop 80 times. Take 1 from each item in fish,
# unless item = 0 in which case set it to 6 and append an 8
for days in range(0, 80): # remember stupid python doesn't run the last loop..
    for fish in range(0, len(fishes)): # for each gives it byval not byref, so need to ref
        # the list directly
        if fishes[fish] == 0:
            fishes[fish] = 6
            fishes.append(8)
        else:
            fishes[fish] -= 1

print(len(fishes))