"""
url = https://adventofcode.com/2020/day/5

Binary Boarding

The first 7 characters will either be F or B; these specify exactly one of the
128 rows on the plane (numbered 0 through 127). Each letter tells you which
half of a region the given seat is in. Start with the whole list of rows; the
first letter indicates whether the seat is in the front (0 through 63) or the
back (64 through 127). The next letter indicates which half of that region the
seat is in, and so on until you're left with exactly one row.
"""


def decode(raw_input):
    """
    Decodes binary encoded strings from input.
    """
    seat_ids = []

    for assign in raw_input:
        """
        Iterates over each boarding pass and determines row number and seat
        position by reducing valid ranges according to input letter.
        """
        row_matrix = assign[:7]
        seat_matrix = assign[7:]

        row_range = list(range(0, 128))
        seat_range = list(range(0, 8))

        for letter in row_matrix:
            if letter == 'F':
                row_range = row_range[:int(len(row_range)/2)]
            else:
                row_range = row_range[int(len(row_range)/2):]

        for letter in seat_matrix:
            if letter == 'L':
                seat_range = seat_range[:int(len(seat_range)/2)]
            else:
                seat_range = seat_range[int(len(seat_range)/2):]

        if row_matrix[6] == 'F':
            row = min(row_range)
        else:
            row = max(row_range)

        if seat_matrix[2] == 'L':
            col = min(seat_range)
        else:
            col = max(seat_range)

        seat_id = (row * 8) + col  # Calculates seat_id according to puzzle
        seat_ids.append(seat_id)

    print('Highest seat ID value:', max(seat_ids))
    part_two(seat_ids)


def part_two(seat_ids):
    """
    What is the ID of your seat?

    Finds the single missing seat_id by iterating over range of unique values
    of all boarding passes.
    """
    for i in range(min(set(seat_ids)), max(set(seat_ids))+1):
        if i not in set(seat_ids):
            print('My seat ID:', i)


if __name__ == '__main__':
    raw_input = []

    # opens corresponding input file, strips newline, adds to input list
    with open('day5.txt', 'r') as fh:
        for item in fh.readlines():
            raw_input.append(item.strip("\n"))

    decode(raw_input)
