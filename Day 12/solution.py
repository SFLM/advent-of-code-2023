from collections import deque
from functools import cache
import copy

def main():
    with open("input.txt") as f:
        data_image = f.read().splitlines()
    
    solution1(data_image)
    solution2(data_image)


def solution1(data_image) -> None:
    total = 0
    for image_row in data_image:
        row, group_info_raw = image_row.split()
        group_info = tuple(int(x) for x in group_info_raw.split(','))

        amount = get_arrangements(row, group_info)
        total += amount
    
    print(f"Solution: {total}")


def solution2(data_image) -> None:
    unfolded_data = []
    for image_row in data_image:
        row, group_info_raw = image_row.split()
        unfolded_row = '?'.join([row]*5)
        unfolded_groups = ','.join([group_info_raw]*5)
        unfolded_data.append(unfolded_row + ' ' + unfolded_groups)

    solution1(unfolded_data)

@cache
def get_arrangements(space_string: str, group_info: tuple):
    string_length = len(space_string)
    if len(group_info) > string_length:
        return 0
    if sum(group_info) > string_length:
        return 0
    if sum(group_info) + len(group_info) > string_length + 1:
        return 0

    first_block_length = group_info[0]
    if len(group_info) == 1:
        return total_fits(space_string, first_block_length, final_block = True)

    # Checks first area that first block fits
    fit_range = []
    other_blocks = group_info[1:]
    other_blocks_minimum_space = sum(other_blocks) + len(other_blocks)
    for i in range(0, string_length - first_block_length + other_blocks_minimum_space + 1):
        if fits(space_string, first_block_length, i):
            fit_range.append(i)

    if not fit_range:
        return 0

    total_arrangements = 0
    for i in fit_range:
        if i + first_block_length + other_blocks_minimum_space <= string_length:
            total_arrangements += get_arrangements(space_string[i + first_block_length + 1:], other_blocks)
        else:
            break

    return total_arrangements


def total_fits(space_string: str, block_length: int, final_block: bool = False):
    total = 0

    for location in range(len(space_string) - block_length + 1):
        if fits(space_string, block_length, location, final_block):
            total += 1
    
    return total


def fits(space_string: str, block_length: int, starting_location: int, final_block: bool = False):
    right_of_block = starting_location + block_length
    string_length = len(space_string)

    if final_block:
        if any(symbol == '#' for symbol in space_string[right_of_block:string_length]): # If final block, check if any occupied spaces to the right
            return False
    if right_of_block > string_length : # Check if block is small enough to fit
        return False
    if starting_location > 0 and any(symbol == '#' for symbol in space_string[0:starting_location]): # Check if any occupied spaces to the left
        return False
    if right_of_block < string_length and space_string[right_of_block] == '#': # Check if space to right is occupied
        return False
    if any(symbol == '.' for symbol in space_string[starting_location:right_of_block]): # Check if any location in block position is blocked
        return False
    return True


if __name__ == "__main__":
    main()
