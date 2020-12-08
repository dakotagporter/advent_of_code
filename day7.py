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

    verify(color_tree)


def verify(color_tree):
    my_bag = 'shiny gold'
    valid_bag = []

    for key in list(color_tree.keys()):
        print(color_tree['dull crimson'])
        for i in range(0, len(color_tree[key])):
            print(color_tree[key])
            bag = color_tree[key][i]
            if bag == 'shiny gold':
                print('has shiny gold!')
                valid_bag.append(key)
            else:
                key = bag
                print(key)


    #print(valid_bag)
    print(color_tree['bright brown'])


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day7.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    filter(raw_input)
