inputFile = open('input.txt').read()

frequency = 0
for line in inputFile.split('\n'):
    frequency += int(line)
print(frequency)