zeroCount = ''
rowCount = 0
itemLength = 0
with open('3.txt') as f:
    for line in f.readlines():
        rowCount += 1
        line = line.rstrip()
        if zeroCount == '':
            # Get the length of each item
            itemLength = len(line)
            zeroCount = list('0'*itemLength)
        # Loop through each character looking for '0's
        pos = 0
        for item in line:
            if item == '0':
                zeroCount[pos]  = str(int(zeroCount[pos])+1)
            pos +=1

print(zeroCount)
print(rowCount)

gamma = list()
epsilon = list()
for item in zeroCount:

    if int(item) < rowCount/2:
        gamma.append('1')
        epsilon.append('0')
    else:
        gamma.append('0')
        epsilon.append('1')

gammaString = ''.join(gamma)
epsilonString = ''.join(epsilon)
result = int(gammaString, 2)*int(epsilonString, 2)
print(result)


        