readings = []

with open('11\\11.txt') as f:
    for line in f.readlines():
        data = line.strip('\n')
        readings.append(list(data))