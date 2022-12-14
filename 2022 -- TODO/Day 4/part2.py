inputFile = open('input.txt', 'r').read()

noOverlaps = 0

for line in inputFile.split('\n'):
    assignments = line.split(',')

    leftFrom = int(assignments[0].split('-')[0])
    leftTo = int(assignments[0].split('-')[1])
    rightFrom = int(assignments[1].split('-')[0])
    rightTo = int(assignments[1].split('-')[1])


    if not (leftTo < rightFrom or rightTo < leftFrom ):
        noOverlaps += 1

print("There are: " + str(noOverlaps) + " not overlapping sections")