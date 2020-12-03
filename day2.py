"""Password Philosophy"""

# url = 'https://adventofcode.com/2020/day/2'

raw_input = []

# opens corresponding input file, strips newline, adds to input list
with open('day2.txt', 'r') as fh:
    for item in fh.readlines():
        raw_input.append(item.strip("\n"))


def split():
    """
    Splits each line into all necessary parts to prep for evaluation.
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
    Verifies puzzle task and returns needed information.
    """
    i = 0

    for x in range(0, len(password)):
        count = password[x].count(letter[x])
        if int(policy_min[x]) <= int(count) <= int(policy_max[x]):
            i += 1

    print(i)


def part_two(policy_min, policy_max, letter, password):
    """
    Verifies puzzle task part two and returns needed information.
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

    print(i)


if __name__ == '__main__':
    split()
