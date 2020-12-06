"""Passport Processing"""

# url = https://adventofcode.com/2020/day/4

import re

raw_input = []

# opens corresponding input file, strips newline, adds to input list
with open('day4.txt', 'r') as fh:
    for item in fh.readlines():
        raw_input.append(item.strip("\n"))


def filter():
    """
    Create each passport by concatenating lines and turning them into their
    inherent key:value pairs.
    """
    passport = ''
    raw_passports = []

    for line in raw_input:
        if line == '':
            raw_passports.append(passport)
            passport = ''
        else:
            passport += ' ' + line
            if line == raw_input[-1]:
                raw_passports.append(passport)

    verify(raw_passports)


def verify(raw_passports):
    """
    Break passport into fields and test conditions.
    """
    count = 0
    valid_passports = []

    for passport in raw_passports:
        fields = passport.strip(' ').split(' ')
        if len(fields) == 8:
            valid_passports.append(passport)
            count += 1
        elif len(fields) == 7 and ('cid' not in passport):
            valid_passports.append(passport)
            count += 1

    print(count)
    part_two(valid_passports)


def part_two(valid_passports):
    i = 0
    dicts = []
    invalid_dicts = []
    valid_dicts = []

    for passport in valid_passports:
        dict = {}
        fields = passport.strip(' ').split(' ')

        for field in fields:
            params = field.split(':')
            dict[params[0]] = params[1]

        dicts.append(dict)

    for dict in dicts:
        if 1920 <= int(dict['byr']) <= 2002:
            pass
        else:
            invalid_dicts.append(dict)
            continue
        if 2010 <= int(dict['iyr']) <= 2020:
            pass
        else:
            invalid_dicts.append(dict)
            continue
        if 2020 <= int(dict['eyr']) <= 2030:
            pass
        else:
            invalid_dicts.append(dict)
            continue
        if dict['hgt'][-2:] in ['cm', 'in']:
            if dict['hgt'][-2:] == 'cm' and 150 <= int(dict['hgt'][:-2]) <= 193:
                pass
            elif dict['hgt'][-2:] == 'in' and 59 <= int(dict['hgt'][:-2]) <= 76:
                pass
        else:
            invalid_dicts.append(dict)
            continue
        if re.match(r'#[\w]{6}', dict['hcl']):
            pass
        else:
            invalid_dicts.append(dict)
            continue
        if dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            invalid_dicts.append(dict)
            continue
        if re.match(r'[\d]{9}', dict['pid']):
            pass
        else:
            invalid_dicts.append(dict)
            continue

        i += 1
        valid_dicts.append(dict)

    print('Valid:', len(valid_dicts))
    print('Invalid:', len(invalid_dicts))
    print('Total:', len(dicts))
    print(i)


if __name__ == '__main__':
    filter()
