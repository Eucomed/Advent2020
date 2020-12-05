import requests


def counteroftrees(down, right):
    row = 0
    col = 0
    count = 0

    while True:
        if rows[row][col] == '#':
            count += 1

        row += down
        col += right

        if row >= len(rows):
            print(str(count))
            return count  # break (end of loop), return (end of loop + return value)

        if col >= len(rows[row]):
            col = col % len(rows[row])


f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/3/input', cookies=cookies)
rows = r.text.split()

# Solution 1
# resultcounteroftrees(1, 3)

# Solution 2
a = counteroftrees(1, 1)
b = counteroftrees(1, 3)
c = counteroftrees(1, 5)
d = counteroftrees(1, 7)
e = counteroftrees(2, 1)
result = a * b * c * d * e

print(result)
