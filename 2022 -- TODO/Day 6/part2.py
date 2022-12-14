inputFile = open('input.txt', 'r').read()

markAfter = 0
found = False

for i in range(len(inputFile)):
    if(not found):
        if not((i - 13) >= 0):
            continue

        buffer = []
        for j in range(14):
            buffer.append(inputFile[i-j])
        
        if len(set(buffer)) == 14:
            markAfter = i + 1
            found = True
    
print(markAfter)