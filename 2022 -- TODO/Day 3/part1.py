inputFile = open('input.txt', 'r').read()

backpackSum = 0

for backpack in inputFile.split('\n'):
    length = len(backpack)

    firstCompartment = sorted(backpack[:int(length/2)])
    secondCompartment = sorted(backpack[int((length/2)):])

    common = [i for i in firstCompartment if i in secondCompartment][0]

    pos = ord(common.lower()) - 97 + 1 # calc pos from 1-26

    if not common.islower(): # lowercase
        pos += 26

    backpackSum += pos

print("The sum is: " + str(backpackSum))