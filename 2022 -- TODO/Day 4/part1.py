inputFile = open('input.txt', 'r').read()

overlaps = 0

for line in inputFile.split('\n'):
    assignments = line.split(',')

    leftFrom = int(assignments[0].split('-')[0])
    leftTo = int(assignments[0].split('-')[1])
    rightFrom = int(assignments[1].split('-')[0])
    rightTo = int(assignments[1].split('-')[1])

    if leftFrom <= rightFrom and rightTo <= leftTo or rightFrom <= leftFrom and leftTo <= rightTo:
        overlaps+=1

print("There are: " + str(overlaps) + " overlaps")