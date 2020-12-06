"""Binary Boarding"""

# url = https://adventofcode.com/2020/day/5

raw_input = []

# opens corresponding input file, strips newline, adds to input list
with open('day5.txt', 'r') as fh:
    for item in fh.readlines():
        raw_input.append(item.strip("\n"))


def decode():
    for assign in raw_input:
        up_row = 128
        low_row = 0

        up_seat = 8
        low_seat = 0

        row = 0
        col = 0

        row_matrix = assign[:7]
        seat_matrix = assign[7:]

        for letter in row_matrix:
            if letter == 'F':
                up_row -= len(range(int(low_row), int(up_row))) / 2
            else:
                low_row += len(range(int(low_row), int(up_row))) / 2

        for letter in seat_matrix:
            print(letter)
            if letter == 'L':
                up_seat -= len(range(int(low_seat), int(up_seat))) / 2
            else:
                up_seat -= len(range(int(low_seat), int(up_seat))) / 2
            print(up_seat, low_seat)
        if row_matrix[6] == 'F':
            row += low_row
        else:
            row += up_row

        if seat_matrix[2] == 'L':
            col += low_seat
        else:
            col += up_seat
        print(col)
        #print(row)




if __name__ == '__main__':
    decode()
