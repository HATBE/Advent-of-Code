inputFile = open('input.txt', 'r').read()

drawing = []
currentLine = []

lines = inputFile.split('\n')
# parse drawing
for line in lines:
    if(line == ''): # if end of drawing -> end loop
        break
    drawing.append(line)

numLineList = list(drawing[-1])

stacks = []

# fill stacks
for line in reversed(lines[:8]):
    index = 0
    for i in range(9):
        stacks.append([])
        if not line[numLineList.index(str((i+1)))] == ' ':
            stacks[i].append(line[numLineList.index(str((i+1)))])
    index+=1

stacks = list(filter(None, stacks))

for line in lines[10:]:
    amount = int(line.split(' ')[1])
    fromLine = int(line.split(' ')[3])
    toLine = int(line.split(' ')[5])

    for i in range(amount):
        popped = stacks[fromLine -1 ].pop(-1)
        stacks[toLine -1 ].append(popped)

word = ''
for stack in stacks:
    word += stack[-1]

print('The word is: ' + str(word))