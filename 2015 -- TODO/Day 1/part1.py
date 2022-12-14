inputFile = open('input.txt', 'r').read()

currentFloor = 0

for char in inputFile:
    if char == ')':
        currentFloor-=1
    elif char == '(':
        currentFloor+=1

print(currentFloor)