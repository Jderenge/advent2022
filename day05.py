f = open('input/day05.txt')
lines = [line.rstrip() for line in f.readlines()]
s1 = ['P', 'D', 'Q', 'R', 'V', 'B', 'H', 'F']
s2 = ['V', 'W', 'Q', 'Z', 'D', 'L']
s3 = ['C', 'P', 'R', 'G', 'Q', 'Z', 'L', 'H']
s4 = ['B', 'V', 'J', 'F', 'H', 'D', 'R']
s5 = ['C', 'L', 'W', 'Z']
s6 = ['M', 'V', 'G', 'T', 'N', 'P', 'R', 'J']
s7 = ['S', 'B', 'M', 'V', 'L', 'R', 'J']
s8 = ['J', 'P', 'D']
s9 = ['V', 'W', 'N', 'C', 'D']
#for line in lines:
sex = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
for i in lines:
    instruct1 = i.split(' ')
    instruct1.remove('move'), instruct1.remove('to'), instruct1.remove('from')
    for x in range(int(instruct1[0])):
        tmp = sex[int(instruct1[1])-1][0]
        sex[int(instruct1[2])-1].insert(0, tmp)
        sex[int(instruct1[1])-1].remove(tmp) 

#part1 = sex
#for i in range(9):
    #print(part1[i][0]),
s1 = ['P', 'D', 'Q', 'R', 'V', 'B', 'H', 'F']
s2 = ['V', 'W', 'Q', 'Z', 'D', 'L']
s3 = ['C', 'P', 'R', 'G', 'Q', 'Z', 'L', 'H']
s4 = ['B', 'V', 'J', 'F', 'H', 'D', 'R']
s5 = ['C', 'L', 'W', 'Z']
s6 = ['M', 'V', 'G', 'T', 'N', 'P', 'R', 'J']
s7 = ['S', 'B', 'M', 'V', 'L', 'R', 'J']
s8 = ['J', 'P', 'D']
s9 = ['V', 'W', 'N', 'C', 'D']
sex = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
for i in lines:
    instruct1 = i.split(' ')
    instruct1.remove('move'), instruct1.remove('to'), instruct1.remove('from')
    for x in range(int(instruct1[0])):
        tmp = sex[int(instruct1[1])-1][0]
        sex[int(instruct1[2])-1].insert(x, tmp)
        sex[int(instruct1[1])-1].remove(tmp)
part2 = sex

for i in range(9):
    print(part2[i][0], end='')
print()
