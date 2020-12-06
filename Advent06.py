import requests
import string

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/6/input', cookies=cookies)

# *** SOLUTION 1 - anyone answered YES ***
# Groups represents groups of combined answers (a-z) delimited by empty row, count letters without their duplicity

groups = r.text[:-1].split('\n\n')  # [:-1] = handling, last character is '\n'
result1 = 0

for group in groups:
    for letter in string.ascii_lowercase:
        if letter in group:
            result1 += 1

print('Counter is thinking ... Bingo! Say yes to see the counter of yes! YES!: ' + str(result1))

# *** SOLUTION 2 - everyone answered YES ***
# Count letters only when appears more time in each row
# Example: (4 x 'a' in four rows = 1, 1 x 'a' in 1 row = 1,'a''b''c' in 3 rows = 0 )

result2 = 0
for group in groups:
    for letter in string.ascii_lowercase:
        if group.count('\n') + 1 == group.count(letter):
            result2 += 1

print('\nOh no. We need to find yes only for group... NO hay problema: ' + str(result2))
