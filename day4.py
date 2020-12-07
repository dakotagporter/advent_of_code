"""
url = https://adventofcode.com/2020/day/4

Passport Processing

Count the number of valid passports - those that have all required fields (byr,
iyr, eyr, hgt, hcl, ecl, pid, cid). Treat 'cid' as optional. In your batch
file, how many passports are valid?
"""

import re


def filter(raw_input):
    """
    Create each passport by concatenating lines from batch file.
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
    Break each passport into fields and test above conditions.
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

    print('Valid Passports (fields):', count)
    part_two(valid_passports)


def part_two(valid_passports):
    """
    You can continue to ignore the cid field, but each other field has strict
    rules about what values are valid for automatic validation:

    - byr (Birth Year) - four digits; at least 1920 and at most 2002.
    - iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    - eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    - hgt (Height) - a number followed by either cm or in:
    - If cm, the number must be at least 150 and at most 193.
    - If in, the number must be at least 59 and at most 76.
    - hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    - ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    - pid (Passport ID) - a nine-digit number, including leading zeroes.
    - cid (Country ID) - ignored, missing or not.

    In your batch file, how many passports are valid?

    Turns each passport into a dictionary and tests values according to above
    parameters.
    """
    i = 0
    dicts = []
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
            continue
        if 2010 <= int(dict['iyr']) <= 2020:
            pass
        else:
            continue
        if 2020 <= int(dict['eyr']) <= 2030:
            pass
        else:
            continue
        if dict['hgt'][-2:] in ['cm', 'in']:
            if dict['hgt'][-2:] == 'cm' and 150 <= int(dict['hgt'][:-2]) <= 193:
                pass
            elif dict['hgt'][-2:] == 'in' and 59 <= int(dict['hgt'][:-2]) <= 76:
                pass
            else:
                continue
        else:
            continue
        if re.match(r'#[a-f0-9]{6}', dict['hcl']):
            pass
        else:
            continue
        if dict['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            pass
        else:
            continue
        if re.match(r'\d{9}', dict['pid']) and len(dict['pid']) == 9:
            pass
        else:
            continue

        i += 1
        
    print('Valid Passports (fields and values):', i)


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day4.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    filter(raw_input)
