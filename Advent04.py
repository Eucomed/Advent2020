import requests
import re

f = open("cookie.txt", "r")
cookies = {'session': f.read()}
r = requests.get('https://adventofcode.com/2020/day/4/input', cookies=cookies)

# Solution 1
validPassports = 0
passports = r.text.split('\n\n')
valid = False

keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
verifiedPasswords = []
for x in range(0, len(passports)):
    for y in range(0, len(keys)):
        if keys[y] in passports[x]:
            valid = True
        else:
            valid = False
            break

    if valid:
        validPassports += 1
        verifiedPasswords.append(passports[x])

# print('Number of valid passport is: ' + str(validPassports))
# print('Number of valid passport is: ' + str(verifiedPasswords))

# Solution 2
goodPswd = 0
for x in range(0, len(verifiedPasswords)):
    tmpArray = re.split(':| |\n', verifiedPasswords[x])
    counter = 0

    for y in range(0, len(tmpArray), 2):
        if tmpArray[y] == 'byr':
            if 1920 <= int(tmpArray[y + 1]) <= 2002:
                counter += 1
            else:
                break

        if tmpArray[y] == 'iyr':
            if 2010 <= int(tmpArray[y + 1]) <= 2020:
                counter += 1
            else:
                break

        if tmpArray[y] == 'eyr':
            if 2020 <= int(tmpArray[y + 1]) <= 2030:
                counter += 1
            else:
                break

        if tmpArray[y] == 'hgt':
            if tmpArray[y + 1][-2:] == 'cm' and 150 <= int(tmpArray[y + 1][:-2]) <= 193:
                counter += 1
            elif tmpArray[y + 1][-2:] == 'in' and 59 <= int(tmpArray[y + 1][:-2]) <= 76:
                counter += 1
            else:
                break

        if tmpArray[y] == 'hcl':
            if len(tmpArray[y + 1]) == 7 and tmpArray[y + 1][0] == '#' and int(tmpArray[y + 1][1:], 16):
                counter += 1
            else:
                break

        if tmpArray[y] == 'ecl':
            if tmpArray[y + 1] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                counter += 1
            else:
                break

        if tmpArray[y] == 'pid':
            if len(tmpArray[y+1]) == 9:
                pattern = '[0-9]{9}'
                result = re.match(pattern, tmpArray[y + 1])

                if result:
                    counter += 1
                else:
                    break
            else:
                break

        if counter == 7:
            counter = 0
            goodPswd += 1

print('Number of valid passport is: ' + str(goodPswd))
