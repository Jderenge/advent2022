f = open('input/day03.txt')
lines = [line.rstrip() for line in f.readlines()]

priority=0
priority2=0
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
    
    
    
for set in range(len(lines)):
    if set % 3 == 0:
        for character in lines[set]:
            if character in lines[set+1] and character in lines[set+2]:
                if character == character.upper():
                    priority2 += ord(character) - ord('A') + 26 + 1
                else:
                    priority2 += ord(character) - ord('a') + 1
                break

                
                
                
        
        
        
part1 = priority
part2 = priority2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
