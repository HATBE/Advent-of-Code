// TODO:
inputFile = open('input.txt', 'r').read()

for line in inputFile.split('\n'):
    encRoomNumber = line[:line.find('[')]
    checksum = line[(line.find('[')+1):-1]

    print(encRoomNumber, checksum)