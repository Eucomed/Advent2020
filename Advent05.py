import requests

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/5/input', cookies=cookies)

# Solution 1
boardPasses = r.text.split('\n')
maxNumber = 0
minNumber = 1000000  # TASK 2
ids = []  # TASK 2

for x in boardPasses[:-1]:  # x = string in boardPasses, [-1] = '', it is not running for [-1]
    x = x.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    row = int(x[:7], 2)
    column = int(x[-3:], 2)
    id = 8 * row + column

    ids.append(id)  # TASK 2

    if id > maxNumber:
        maxNumber = id

    if id < minNumber:  # TASK 2
        minNumber = id


for z in range(minNumber, maxNumber):  # TASK 2
    if z not in ids:
        print("Your seat is: " + str(z))

print(maxNumber)
