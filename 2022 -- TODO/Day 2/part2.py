inputFile = open('input.txt', 'r').read()

scoreMap = {
    'A': 1, # Rock
    'B': 2, # Paper
    'C': 3, # Scissors
}

winMap = {
    'A': 'B',
    'B': 'C',
    'C': 'A'
}

looseMap = {
    'A': 'C',
    'B': 'A',
    'C': 'B'
}

drawMap = {
    'A': 'A',
    'B': 'B',
    'C': 'C'
}

score = 0

for line in inputFile.split('\n'):
    chars = line.split(' ')

    him = chars[0]
    behavior = chars[1]

    if behavior == 'X': # loose
        score += scoreMap[looseMap[him]]
    elif behavior == 'Y': # draw
        score += 3 + scoreMap[drawMap[him]]
    elif behavior == 'Z': # win
        score += 6 + scoreMap[winMap[him]]

print("Your score is: " + str(score))