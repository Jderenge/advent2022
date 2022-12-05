f = open('input/day01.txt')
lines = [line.rstrip() for line in f.readlines()]

calorie =0
elfs = []

for line in lines:
    if line!='':
        calorie = calorie + int(line)
    else:
        elfs.append(calorie)
        calorie = 0
        
    #print(line)

top3 = []
part1 = max(elfs)
top3 = max(elfs)
elfs.pop(elfs.index(max(elfs)))
top3+=max(elfs)
elfs.pop(elfs.index(max(elfs)))
top3+=max(elfs)


part2 = top3

print(f'part 1: {part1}')
print(f'part 2: {part2}')