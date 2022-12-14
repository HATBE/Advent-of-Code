inputFile = open('input.txt', 'r').read()

total = 0

for line in inputFile.split('\n'):
    sizesArray = line.split('x')

    l = int(sizesArray[0])
    w = int(sizesArray[1])
    h = int(sizesArray[2])

    total += (2* (l*w + w*h + h*l)) + min(l*w,l*h,w*h)

print(total)