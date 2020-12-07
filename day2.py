"""
url = 'https://adventofcode.com/2020/day/2'

Password Philosophy

Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear for
the password to be valid. For example, 1-3 a means that the password must
contain a at least 1 time and at most 3 times. How many passwords are valid
according to their policies?
"""


def split(raw_input):
    """
    Splits each line into policy, letter and password for verification.
    """
    policy_min = []
    policy_max = []
    letter = []
    password = []

    for item in raw_input:
        part = item.split(" ")
        policy_min.append(part[0].split("-")[0])
        policy_max.append(part[0].split("-")[1])
        letter.append(part[1].strip(":"))
        password.append(part[2])

    verify(policy_min, policy_max, letter, password)
    part_two(policy_min, policy_max, letter, password)


def verify(policy_min, policy_max, letter, password):
    """
    Verifies password according to above parameters.
    """
    i = 0

    for x in range(0, len(password)):
        count = password[x].count(letter[x])
        if int(policy_min[x]) <= int(count) <= int(policy_max[x]):
            i += 1

    print('Valid Passwords (count):', i)


def part_two(policy_min, policy_max, letter, password):
    """
    Each policy actually describes two positions in the password, where 1 means
    the first character, 2 means the second character, and so on. (Be careful;
    Toboggan Corporate Policies have no concept of "index zero"!) Exactly one
    of these positions must contain the given letter. Other occurrences of the
    letter are irrelevant for the purposes of policy enforcement.

    Verifies password according to above parameters.
    """
    i = 0

    for x in range(0, len(password)):
        positions = [password[x][int(policy_min[x])-1],
                     password[x][int(policy_max[x])-1]]
        if letter[x] == positions[0] or letter[x] == positions[1]:
            if letter[x] == positions[0] and letter[x] == positions[1]:
                pass
            else:
                i += 1

    print('Valid Passwords (position):', i)


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day2.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    split(raw_input)
