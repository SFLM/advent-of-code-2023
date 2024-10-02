from functools import cache
from typing import Union
import time

CUBE_LOCATIONS = dict()
PATTERNS = dict()

def main():

    with open("input.txt") as f:
        data = tuple(f.read().splitlines())

    initialize_cube_locations(data)
    
    solution1(data)
    solution2(data)


def solution1(raw_data: tuple) -> None:
    start_time = time.time()
    tilted_data = tilt(raw_data)
    answer = get_total_load(tilted_data)
    end_time = time.time()

    print(f"Solution 1: {answer}, time elapsed: {end_time - start_time}")


def solution2(data) -> None:
    global PATTERNS

    ROTATIONS = 1000000000
    start_time = time.time()
    rotated_data = get_rotated_result(data, ROTATIONS)
    answer = get_total_load(rotated_data)
    end_time = time.time()

    print(f"Solution 2: {answer}, time elapsed: {end_time - start_time}")


def get_rotated_result(data: tuple, initial_rotations: int) -> tuple:
    rotations = initial_rotations

    rotated_data = data
    while rotations > 0:
        if rotated_data in PATTERNS:
            pattern_length = len(PATTERNS[rotated_data])
            if pattern_length <= rotations:
                final_rotations = rotations % pattern_length
                return PATTERNS[rotated_data][final_rotations - 1]
            return PATTERNS[rotated_data][rotations - 1]

        result = rotate(rotated_data)
        PATTERNS.update({rotated_data: []})
        for input in PATTERNS:
            PATTERNS[input].append(result)
        rotated_data = result
        rotations -= 1
    
    return rotated_data


def initialize_cube_locations(data: tuple) -> None:
    global CUBE_LOCATIONS
    for row_index, row in enumerate(data):
        CUBE_LOCATIONS.update({f"Row {row_index}": get_cube_locations(row)})
    for column_index, column in enumerate(tuple([*zip(*data)])):
        CUBE_LOCATIONS.update({f"Column {column_index}": get_cube_locations(column)})


@cache
def rotate(raw_data: tuple) -> tuple:
    new_data = raw_data
    for direction in range(4):
        new_data = tilt(new_data, direction)
    
    return new_data


@cache
def tilt(raw_data: tuple, direction: int = 0) -> tuple: # North, West, South, East

    new_data = []

    if direction == 0: # North
        for column_index, column in enumerate(tuple([*zip(*raw_data)][::-1])): # (rotates left, no reverse)
            new_data.append(tilt_row(column, column_index, False))
        
        return tuple([*zip(*new_data[::-1])])
    if direction == 1: # West
        for row_index, row in enumerate(raw_data): # (no rotation, no reverse)
            new_data.append(tilt_row(row, row_index, True))
        
        return tuple(new_data)
    if direction == 2: # South
        for column_index, column in enumerate(tuple([*zip(*raw_data)][::-1])): # (rotates left, reverse)
            new_data.append(tilt_row(column, column_index, False, True))
        
        return tuple([*zip(*new_data[::-1])])
    else: # East
        for row_index, row in enumerate(raw_data): # (no rotation, reverse)
            new_data.append(tilt_row(row, row_index, True, True))
        
        return tuple(new_data)


@cache
def tilt_row(row: Union[tuple, str], row_number_raw: int, is_row: bool = True, reverse: bool = False) -> str:
    global CUBE_LOCATIONS

    row_length = len(row)
    if not is_row:
        row_number = row_length - row_number_raw - 1
    else:
        row_number = row_number_raw

    if is_row:
        angle = "Row "
    else:
        angle = "Column "
    row_cubes = CUBE_LOCATIONS[angle + str(row_number)]

    if len(row_cubes) == 0:
        rock_amount = row.count('O')
        rock_string = 'O' * rock_amount
        space_string = '.' * (row_length - rock_amount)
        if reverse:
            return space_string + rock_string
        return rock_string + space_string

    new_row = ""
    last_barrier = 0
    rock_amount = 0
    for cube_location in row_cubes:
        rock_amount = row[last_barrier:cube_location].count('O')
        rock_string = 'O' * rock_amount
        space_string = '.' * (cube_location - rock_amount - last_barrier)
        if reverse:
            new_row += space_string + rock_string
        else:
            new_row += rock_string + space_string
        new_row += '#'
        last_barrier = cube_location + 1

    rock_amount = row[last_barrier:row_length].count('O')
    rock_string = 'O' * rock_amount
    space_string = '.' * (row_length - rock_amount - last_barrier)
    if reverse:
        new_row += space_string + rock_string
    else:
        new_row += rock_string + space_string
    return new_row


def get_cube_locations(data_row: Union[tuple, str]) -> tuple:
    return tuple([index for index, symbol in enumerate(data_row) if symbol == '#'])


def get_total_load(data: tuple) -> int:
    total_weight = 0

    load_value = len(data)
    for row in data:
        total_weight += row.count('O') * load_value
        load_value -= 1
    return total_weight


if __name__ == "__main__":
    main()
