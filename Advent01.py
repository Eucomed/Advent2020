import requests

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/1/input', cookies=cookies)

numbers = r.text.split()
print(r.text)

# Solution for 1. task
for x in range(0, len(numbers)):
    for y in range(x+1, len(numbers)):
        if int(numbers[x]) + int(numbers[y]) == 2020:
            print('Your magic numbers are: ' + str(numbers[x]) + ' and ' + str(numbers[y]) + '.')
            magicWord = int(numbers[x]) * int(numbers[y])
            print('and your magic password to the next level is: ' + str(magicWord) + '.')

# Solution for 2. task
for x in range(0, len(numbers)):
    for y in range(x+1, len(numbers)):
        for z in range(y+1, len(numbers)):
            if int(numbers[x]) + int(numbers[y]) + int(numbers[z]) == 2020:
                print('Your magic numbers are: ' + str(numbers[x]) + ' and ' + str(numbers[y]) + ' and wait for it ' + str(numbers[z]) + '.')
                magicWord2 = (int(numbers[x]) * int(numbers[y]) * int(numbers[z]))
                print('and after this password you can already go to the bed ' + str(magicWord2) + '.')




