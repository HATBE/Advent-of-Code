inputFile = open('input.txt', 'r').read()

elves = []
count = 0
currentElf = []

for line in inputFile.split('\n'):
    if line == '':
        if currentElf != []:
            calories = 0
            for calorie in currentElf:
                calories+=int(calorie)
            elves.append(calories)
        count+=1
        currentElf = []
    else:
        currentElf.append(line)

elves.sort(reverse=True)

print('The three elfves with the max calories togetehr has "' + str(elves[0]+elves[1]+elves[2]) + '" calories.')