f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

priority=0
for line in lines:
    firsthalf = line[:len(line)//2]
    secondhalf = line[len(line)//2:]
    #print(line)
    
    for character in firsthalf:
        if character in secondhalf:
            if character == character.upper():
                priority += ord(character) - ord('A') + 26 + 1
            else:
                priority += ord(character) - ord('a') + 1
            break
        
    for character in line[1,2,3]:
        
        
part1 = priority
part2 = 0

print(f'part 1: {part1}')
print(f'part 2: {part2}')
