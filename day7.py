"""
url = 'https://adventofcode.com/2020/day/7'

Handy Haversacks

Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and must
contain specific quantities of other color-coded bags. Apparently, nobody
responsible for these regulations considered how long they would take to
enforce!
"""


def filter(raw_input):
    """
    Creates the hierarchy of colors by splitting their requirements and turning
    each on into a dictionary with the main color as the key and the colors it
    must contain as the values.
    """
    values = []
    color_tree = {}
    for line in raw_input:
        words = line.split(' ')
        key = ' '.join(words[:2])
        for i in range(0, len(words)):
            if words[i].isnumeric():
                sub_color = words[i+1:i+3]
                values.append(' '.join(sub_color))

        color_tree[key] = values
        values = []

    #verify(color_tree)
    part_two(color_tree)


def verify(color_tree):
    """
    Iterates through every key and determines if it contains any bags that
    directly contain a shiny gold bag.
    """
    my_bag = 'shiny gold'
    valid_bags = []

    for key in color_tree.keys():
        if my_bag in color_tree[key]:
            valid_bags.append(key)

    for bag in valid_bags:
        for key in color_tree.keys():
            if bag in color_tree[key]:
                valid_bags.append(key)

    print('Number of bags eventually containing a shiny gold bag:',
          len(set(valid_bags)))


def part_two(color_tree):
    color_tree['shiny gold']


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day7.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    filter(raw_input)
