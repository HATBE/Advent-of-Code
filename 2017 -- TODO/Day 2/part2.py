inputFile = open('input.txt', 'r').read()

count = 0

for line in inputFile.split('\n'):
    nums = []
    for num in line.split('\t'):
        nums.append(int(num))
    
    for num1 in nums:
        for num2 in nums:
            if num1 == num2:
                continue
            if num1 % num2 == 0:
                count += round(num1 / num2)

print(count)