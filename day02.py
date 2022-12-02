f = open('input/day02.txt')
lines = [line.rstrip() for line in f.readlines()]
score =0
scorep2 =0
for line in lines:
    a, b= line.split()
    if (a=='A' and b =='X') or (a=='B' and b =='Y') or (a=='C' and b =='Z'):
        score += 3
    elif (a=='A' and b =='Z') or (a=='B' and b =='X') or (a=='C' and b =='Y'):
        score += 0
    elif (a=='A' and b =='Y') or (a=='B' and b =='Z') or (a=='C' and b =='X'):
        score += 6
    
    if b=='X':score+=1
    elif b=='Y':score+=2
    else: score+=3
    
    # How to lose
    if b=='X':
        if a=='A':
            b='Z'
        elif a=='B':
            b='X'
        elif a=='C':
            b='Y'
    # How to win
    elif b=='Z':
        if a=='A':
            b='Y'
        elif a=='B':
            b='Z'
        elif a=='C':
            b='X'
    # How to tie
    elif b=='Y':
        if a=='A':
            b='X'
        elif a=='B':
            b='Y'
        elif a=='C':
            b='Z'

    if (a=='A' and b =='X') or (a=='B' and b =='Y') or (a=='C' and b =='Z'):
        scorep2 += 3
    elif (a=='A' and b =='Z') or (a=='B' and b =='X') or (a=='C' and b =='Y'):
        scorep2 += 0
    elif (a=='A' and b =='Y') or (a=='B' and b =='Z') or (a=='C' and b =='X'):
        scorep2 += 6
    
    if b=='X':scorep2+=1
    elif b=='Y':scorep2+=2
    else: scorep2+=3
            

part1 = score
part2 = scorep2

print(f'part 1: {part1}')
print(f'part 2: {part2}')
