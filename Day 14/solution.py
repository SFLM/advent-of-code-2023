from collections import deque
from functools import cache

def main():
    with open("input.txt") as f:
        data = f.read().splitlines()
    
    solution1(data)
    # solution2(data)


def solution1(data) -> None:
    total_weight = 0
    row_amt, col_amt = (len(data), len(data[0]))

    column_heights_dict = {pos: 0 for pos in range(col_amt)}
    new_data = [['.' for _ in range(col_amt)] for _ in range(row_amt)]

    for vertical_position, row in enumerate(data):
        # print(row)
        for horizontal_position, symbol in enumerate(row):
            if symbol == 'O':
                # print(f"'O' found on row {vertical_position}, col {horizontal_position};;; changing row {vertical_position}, col {column_heights_dict[horizontal_position]}")
                new_data[column_heights_dict[horizontal_position]][horizontal_position] = 'O'
                column_heights_dict[horizontal_position] += 1
            elif symbol == '#':
                new_data[vertical_position][horizontal_position] = '#'
                column_heights_dict[horizontal_position] = vertical_position + 1
    
    load_value = row_amt
    for row in new_data:
        total_weight += row.count('O') * load_value
        load_value -= 1
    
    print(f"Solution 1: {total_weight}")


def solution2(data) -> None:
    pass


if __name__ == "__main__":
    main()
