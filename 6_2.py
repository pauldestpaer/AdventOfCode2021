def sumUpTheFish(testFishes):
    total = 0
    for v in testFishes.values():
        total += v

    return total

fishes = []
import os
print(os.getcwd())
with open('6\\6.txt') as f:
    for line in f.readlines():
        # just one line to read here. Split it by ','...
        splitLine = line.split(',')
        # And feed it into the array
        for item in splitLine:
            fishes.append(int(item))

# Now, loop 256 times. Take 1 from each item in fish,
# unless item = 0 in which case set it to 6 and append an 8
# for days in range(0, 256): # remember stupid python doesn't run the last loop..
#     for fish in range(0, len(fishes)): # for each gives it byval not byref, so need to ref
#         # the list directly
#         if fishes[fish] == 0:
#             fishes[fish] = 6
#             fishes.append(8)
#         else:
#             fishes[fish] -= 1

# cunning. The number is too large to run on a normal pc, so needs calculating a different way

# any fish that generates a new fish will generate another new fish in 7 turns. Any fish that
# is generated will generate its first new fish in 9 turns.
  

testFishes = {}
testFishes[0] = 1
fishProduced = {}
totalFish = 0

for fish in fishes:
    testFishes = {}
    testFishes[fish] = 1
    for day in range(0, 256):
        # Find all the matching fish. That then creates a new fish age + 9 and sets the next
        # fish creation date for that fish by +7
            if day not in testFishes:
                continue # Handles early cases where there are no fish
            todayCount = testFishes[day]
            # Add the restart total
            if (day+7) not in testFishes:
                testFishes[day+7] = todayCount
            else:
                testFishes[day+7] += todayCount
            # Add the new total
            testFishes[day+9] = todayCount
            # remove the total for ths day, they've been moved to day+7
            testFishes[day] = 0

    totalFish += sumUpTheFish(testFishes) 



print (totalFish)