inputFile = open('input.txt', 'r').read()

dirs = {}

lastDir = '/'
goneUp = 0
for line in inputFile.split('\n'):
    if line[0] == '$':
        # line is command
        command = line.split(' ')

        if command[1] == 'cd': # changes directory
            changeToPath = command[2]

            if changeToPath == '..': # go up one directory
                goneUp += 1
            else:
                if goneUp >= 0:
                    dirs[lastDir][changeToPath] = {}
                lastDir = changeToPath
                goneUp = 0

print(dirs)