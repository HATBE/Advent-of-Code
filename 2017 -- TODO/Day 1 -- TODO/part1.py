inputFile = open('input.txt').read()

count = 0
lastChar = 0

for char in inputFile:
    if char == lastChar:
        count+=int(char)
    
    lastChar = char

count+=int(inputFile[-1])

print(count)