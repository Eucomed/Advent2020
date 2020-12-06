import requests
import string

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/6/input', cookies=cookies)

# Solution 1 - anyone answered YES
input = r.text[:-1].split('\n\n')  # [:-1] = handling, last character is '\n'
counterYes = 0

for x in input:
    for y in string.ascii_lowercase:
        if y in x:
            counterYes += 1

print('Counter is thinking ... Bingo! Say yes to see the counter of yes! YES!: ' + str(counterYes))

# Solution 2 - everyone answered YES
everyoneYes = 0
for x in input:
    for letter in string.ascii_lowercase:
        if letter in x:
            if x.count('\n') + 1 == x.count(letter):
                everyoneYes += 1

print('\nOh no. We need to find yes only for group... NO hay problema: ' + str(everyoneYes))
