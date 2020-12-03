"""Report Repair"""

# url = "https://adventofcode.com/2020/day/1"

raw_input = []

# opens corresponding input file, strips newline, adds to input list
with open('day1.txt', 'r') as fh:
    for item in fh.readlines():
        raw_input.append(item.strip("\n"))


def verify():
    """
    Sums and multiplies numbers according to puzzle task.
    """
    for num in raw_input:
        for num2 in raw_input:
            if int(num) + int(num2) == 2020:
                print(int(num)*int(num2))
                break


def part_two():
    """
    Sums and multiplies numbers according to puzzle task.
    """
    for num in raw_input:
        for num2 in raw_input:
            for num3 in raw_input:
                if int(num) + int(num2) + int(num3) == 2020:
                    print(int(num)*int(num2)*int(num3))
                    break


if __name__ == '__main__':
    verify()
    part_two()
