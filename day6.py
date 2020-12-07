"""
url = 'https://adventofcode.com/2020/day/6'

Custom Customs

The form asks a series of 26 yes-or-no questions marked a through z. All you
need to do is identify the questions for which anyone in your group answers
"yes". Each group's answers are separated by a blank line, and within each
group, each person's answers are on a single line. For each group, count the
number of questions to which anyone answered "yes". What is the sum of those
counts?
"""

import re


def filter(raw_input):
    """
    Combine lines for each group. Sum the unique values of each answer.
    """
    forms = []
    answers = []
    count = []

    for line in raw_input:
        if line != '':
            answers.append(line)
            if line == raw_input[-1]:
                forms.append(answers)
        else:
            forms.append(answers)
            answers = []

    for form in forms:
        letters = ''.join(form)
        num_yes = len(set(letters))
        count.append(num_yes)

    print('Sum of unique "yes" answers:', sum(count))
    part_two(forms)


def part_two(forms):
    count = []
    duplicates = []

    for form in forms:
        for letter in form[0]:
            for form in forms:
                if letter in form:
                    if form == forms[-1]:
                        duplicates.append(letter)
                    else:
                        continue
                else:
                    break

    print('Sum of answers where ALL members answered "yes:', sum(count))


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day6.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    filter(raw_input)
