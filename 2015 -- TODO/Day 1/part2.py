inputFile = open('input.txt', 'r').read()

currentFloor = 0

index = 1
for char in inputFile:
    if char == ')':
        currentFloor-=1
    elif char == '(':
        currentFloor+=1

    if currentFloor == -1:
        print(index)
        break

    index+=1