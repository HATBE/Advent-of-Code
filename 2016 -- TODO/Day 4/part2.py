inputFile = open('input.txt', 'r').read()

for line in inputFile.split('\n'):
    encRoomNumber = line[:(line.find('[')-4)]
    checksum = line[(line.find('[')+1):-1]
    sectorNumber = int(line[-10:-7])

    mostUsed = sorted(''.join(encRoomNumber.split('-')))

    # get most used
    charList = {}
    for char in mostUsed:
        if(char not in charList):
            charList[char] = 1
        else:
            charList[char] += 1

    mu = dict(sorted(charList.items(), key=lambda x:x[1], reverse=True))
    mu = list(mu.keys())

    mostUsedKey = ''.join(mu[:5])


    if mostUsedKey == checksum: # valid room
        realName = ''
        for char in encRoomNumber.replace('-', ' '):
            realName += ''.join(chr((ord(char) - 97 + sectorNumber) % 26 + 97))

        if "northpole" in realName:
            print(sectorNumber)
            exit()