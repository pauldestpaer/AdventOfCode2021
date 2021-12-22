
totalRowCount = 0
itemLength = 0
digits = []
allTheData = []
with open('3.txt') as f:
    for line in f.readlines():
        # this time, read them all into a set. Will need to go through them multiple times
        allTheData.append(line.rstrip())
        totalRowCount +=1
rowCount = totalRowCount
# Go through the set and select the items matching the digit from the
# nominated position. Remove the rest. Repeat until only 1 left
dataForO2 = allTheData.copy()
for posToCheck in range(len(line)): # = for 0 to len(line) - 1
    # Check we aren't done
    if rowCount == 1:
        break

    zeroCount = 0
    # Check the set's contents at the specified position
    for data in dataForO2:
        if data[posToCheck] == '0':
            zeroCount += 1

    if zeroCount <= rowCount/2:
        removeValue = '0'
        digits.append('1')
    else:
        removeValue = '1'
        digits.append('0')
    # Now remove the matching elements. List comprehension
    dataForO2 = [x for x in dataForO2 if x[posToCheck] != removeValue]
    rowCount = len(dataForO2)

print(digits)
print(dataForO2)

digits = []

# repeat for least common
rowCount = totalRowCount
dataForCO2 = allTheData.copy()
for posToCheck in range(len(line)): # = for 0 to len(line) - 1
    # Check we aren't done
    if rowCount == 1:
        break

    zeroCount = 0
    # Check the set's contents at the specified position
    for data in dataForCO2:
        if data[posToCheck] == '0':
            zeroCount += 1

    if zeroCount > rowCount/2:
        removeValue = '0'
        digits.append('1')
    else:
        removeValue = '1'
        digits.append('0')
    # Now remove the matching elements. List comprehension
    dataForCO2 = [x for x in dataForCO2 if x[posToCheck] != removeValue]
    rowCount = len(dataForCO2)

print(digits)
print(dataForCO2)

# Should now have juwst one number
dataForCO2String = ''.join(dataForCO2)
dataForO2String = ''.join(dataForO2)
result = int(dataForCO2String, 2)*int(dataForO2String, 2)
print(result)

        