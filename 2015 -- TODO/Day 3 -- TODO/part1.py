inputFile = open('input.txt', 'r').read()

coordsX = 0
coordsY = 0

coordsMap = {}

multi = 0

for direction in inputFile:
    if coordsX not in coordsMap: # new x index
        coordsMap[coordsX] = {} 
    
    if coordsY not in coordsMap[coordsX]: # new y index
        coordsMap[coordsX][coordsY] = 1
    else: # index already exists
        coordsMap[coordsX][coordsY] += 1

    if direction == '^': # north
        coordsY += 1
    elif direction == 'v': # south
        coordsY -= 1
    elif direction == '>': # east
        coordsX += 1
    elif direction == '<': # west
        coordsX -= 1

for x in coordsMap:
    for y in coordsMap[x]:
        multi += 1

print(multi)