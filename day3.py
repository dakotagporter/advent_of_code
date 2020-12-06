"""Toboggan Trajectory"""

# url = https://adventofcode.com/2020/day/3

raw_input = []

# opens corresponding input file, strips newline, adds to input list
with open('day3.txt', 'r') as fh:
    for item in fh.readlines():
        raw_input.append(item.strip("\n"))

course = ''
for line in raw_input:
    course += line

def slope1():
    pos = 0
    count = 0
    for square in course:
        pos += (len(raw_input[0]) + 3)
        char = course[pos]
        if char == '#':
            count += 1
            print(count)
        else:
            print(char)
        if pos == len(course):
            break


def slope():
    row = 0
    col = 0
    count = 0

    for i in range(0, len(raw_input)-1):
        row += 1
        col += 3
        square = raw_input[row][col]
        print(row, col)
        if square == '#':
            count += 1
        if col == len(raw_input[0]):
            pass

    print(count)


if __name__ == '__main__':
    slope1()
