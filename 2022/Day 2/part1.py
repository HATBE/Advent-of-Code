inputFile = open('input.txt', 'r').read()

scoreMap = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3, # Scissors
}

# 0 = draw, 1 = win, 2 = loose
outcomeMap = {
    'AX': 0,
    'AY': 1,
    'AZ': 2,
    'BX': 2,
    'BY': 0,
    'BZ': 1,
    'CX': 1,
    'CY': 2,
    'CZ': 0
}

score = 0

for line in inputFile.split('\n'):
    chars = line.split(' ')

    him = chars[0]
    me = chars[1]

    outcome = outcomeMap[str(him+me)]

    if outcome == 0: # draw
        score += 3 + scoreMap[me]
    elif outcome == 1: # me win
        score += 6 + scoreMap[me]
    elif outcome == 2: # me loose
        score += scoreMap[me]

print("Your score is: " + str(score))