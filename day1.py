"""
url = "https://adventofcode.com/2020/day/1"

Report Repair

Find the two entries that sum to 2020 and then multiply those two numbers
together.
"""


def verify(raw_input):
    """
    Sums and multiplies numbers according to above parameters.
    """
    for num in raw_input:
        for num2 in raw_input:
            if int(num) + int(num2) == 2020:
                print('Product of the two numbers whose sum is 2020:',
                      int(num)*int(num2))
                break


def part_two(raw_input):
    """
    Find the three entries that sum to 2020 and then multiply those three
    numbers together.

    Sums and multiplies numbers according to above parameters.
    """
    for num in raw_input:
        for num2 in raw_input:
            for num3 in raw_input:
                if int(num) + int(num2) + int(num3) == 2020:
                    print('Product of the three numbers whose sum is 2020:',
                          int(num)*int(num2)*int(num3))
                    break


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day1.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    verify(raw_input)
    part_two(raw_input)
