inputFile = open('input.txt', 'r').read()

checksum = 0

for line in inputFile.split('\n'):
    nums = []
    for num in line.split('\t'):
        nums.append(int(num))
    
    checksum += max(nums) - min(nums)
    
print(checksum)