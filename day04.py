f = open('input/day04.txt')
lines = [line.rstrip() for line in f.readlines()]

import re

part1 = 0
part2 = 0

for line in lines:
    line = [int(n) for n in re.split(",|-",line)]
    
    elf_sex = set(range(line[0],line[1]+1)) 
    elf_cum = set(range(line[2],line[3]+1))
    if elf_sex.issubset(elf_cum) or elf_cum.issubset(elf_sex):
        part1 +=1
    if elf_sex.intersection(elf_cum):
        part2 +=1
        
        
        
    


print(f'part 1: {part1}')
print(f'part 2: {part2}')
