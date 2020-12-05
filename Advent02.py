import requests
import re

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/2/input', cookies=cookies)

s = re.split('-| |: |\n', r.text)

# Solution for 1. task
count = 0
for x in range(0, len(s) - 1, 4):
    stringCounter = s[x + 3].count(s[x + 2])
    if int(s[x]) <= stringCounter <= int(s[x + 1]):
        count = count + 1
print(count)

# Solution for 2. task
count1 = 0

for x in range(0, len(s)-1, 4):
    a = int(s[x])
    b = int(s[x + 1])
    c = s[x + 2]
    d = s[x + 3]

    if d[a-1] == c ^ d[b-1] == c:
        count1 = count1 + 1

print(count1)
