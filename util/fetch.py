#!/usr/bin/python3

from datetime import datetime, timezone, timedelta
from sys import argv
from bs4 import BeautifulSoup
import requests

year, day = datetime.now(timezone(timedelta(hours=-5))).year, \
            datetime.now(timezone(timedelta(hours=-5))).day

if len(argv) == 2:
    day = int(argv[1])
if len(argv) == 3:
    year, day = int(argv[1]), int(argv[2])

# firefox: ctrl+shift+i, storage, cookies, copy value of session

cookie = open('util/cookie.txt', 'r').readline().strip()
finput = open(f'input/day{day:0>2}.txt', 'w+')
ftest = open(f'test/day{day:0>2}.txt', 'w+')

# use responsibly! advent of code is frequently inundated with exceessive
# requests. there is a 15 minute cooldown on requests to prevent you from 
# potentially being banned.

# for i in {1..25}; do ./util/fetch.py 2021 $i; sleep 900; done

throttle = float(open('util/throttle.txt', 'r').readline().strip())
if datetime.timestamp(datetime.now()) - throttle >= 15 * 60:
    throttle = False
else:
    throttle = int((15 * 60) - (datetime.timestamp(datetime.now()) - throttle))
    print(f'throttling requests for another {throttle} seconds')
    exit()

if finput.read() == '':
    print('fetching input...')
    input = f'https://adventofcode.com/{year}/day/{day}/input'
    input = requests.get(input, cookies={'session': cookie}).text
    throttle = True
else:
    print('input found on disk. not fetching')
    input = finput.read()
if ftest.read() == '':
    print('fetching test...')
    test = f'https://adventofcode.com/{year}/day/{day}'
    test = requests.get(test, cookies={'session': cookie}).text
    throttle = True
else:
    print('test found on disk. not fetching')
    test = ftest.read()

try:
    print('analyzing test candidates...')
    soup = BeautifulSoup(test, 'html.parser')
    test = soup.select('article > pre > code')

    # simple character analysis on candidates for test inputs. works maybe 90%
    # of the time. if it doesn't work, manually find the test input

    bestcase = [test[0].text, 0, 0]
    for case in test:
        case, forwards, backwards = case.text, 0, 0
        for c in case:
            forwards += 1 if c in input else 0
        for i in range(min(len(input), 1000)):
            backwards += 1 if input[i] in case else 0

        bestcase = [case, forwards, backwards] if backwards > bestcase[2] else bestcase
    
    test = bestcase[0]
    bestcase[1] /= len(bestcase[0])
    bestcase[2] /= min(len(input), 1000)

    if (abs(bestcase[1] - bestcase[2]) > 0.3):
        print('test input may not be valid. check manually')
        print(f'https://adventofcode.com/{year}/day/{day}')

except IndexError:
    print('test input is not valid. check manually')
    print(f'https://adventofcode.com/{year}/day/{day}')
    test = ''

finput.write(input)
ftest.write(test)

if throttle:
    f = open('util/throttle.txt', 'w')
    f.write(str(datetime.timestamp(datetime.now())) + '\n')
