inputFile = open('input.txt', 'r').read()

groupSum = 0

groups = []

groupCount = 0
currentGroup = []

for backpack in inputFile.split('\n'):
    groupCount += 1

    backpack = sorted(backpack)

    currentGroup.append(backpack)

    if groupCount >= 3:
        groups.append(currentGroup)
        groupCount = 0
        currentGroup = []

for group in groups:
    common = [i for i in [i for i in group[0] if i in group[1]] if i in group[2]][0]
    
    pos = ord(common.lower()) - 97 + 1 # calc pos from 1-26

    if not common.islower(): # lowercase
        pos += 26
    
    groupSum += pos

print("The sum is: " + str(groupSum))