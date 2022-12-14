inputFile = open('input.txt', 'r').read()

total = 0

for line in inputFile.split('\n'):
    sizesArray = line.split('x')

    l = int(sizesArray[0])
    w = int(sizesArray[1])
    h = int(sizesArray[2])

    total += min(l+l+w+w, l+l+h+h, w+w+h+h) + (l * w * h)

print(total)