"""
url = 'https://adventofcode.com/2020/day/7'

Handy Haversacks

Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take to
enforce!
"""


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day4.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    filter(raw_input)
