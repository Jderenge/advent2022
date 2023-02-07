f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

part1 = 0
part2 = 0

for line in lines:
    line = [int(n) for n in re.split(",|-",line)]
    
    elf = set(range(line[0],line[1]+1)) 
    elfs = set(range(line[2],line[3]+1))
    if elf.issubset(elfs) or elfs.issubset(elf):
        part1 +=1
    if elf.intersection(elfs):
        part2 +=1
    
        
        
    


print(f'part 1: {part1}')
print(f'part 2: {part2}')
