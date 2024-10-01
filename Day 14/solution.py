from functools import cache
from typing import Union

CUBE_LOCATIONS = dict()

def main():

    with open("example.txt") as f:
        data = tuple(f.read().splitlines())

    initialize_cube_locations(data)
    
    # solution1(data)
    solution2(data)


def solution1(raw_data: tuple) -> None:
    tilted_data = tilt(raw_data)
    for row in tilted_data:
        print(row)
    print(f"Solution 1: {get_total_load(tilted_data)}")


def solution2(data) -> None:
    rotated_data = data

    ROTATIONS = 1000000
    for _ in range(ROTATIONS):
        rotated_data = rotate(rotated_data)
    
    for row in rotated_data:
        print(row)

    print(f"Solution 2: {get_total_load(rotated_data)}")


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
        new_data = tuple(tilt(new_data, direction))
    
    return new_data


@cache
def tilt(raw_data: tuple, direction: int = 0) -> tuple: # North, West, South, East
    new_data = []

    if direction == 0: # North
        for column_index, column in enumerate(tuple([*zip(*raw_data)][::-1])): # (rotates left, no reverse)
            new_data.append(tilt_row(column, column_index, False))
        
        return [*zip(*new_data[::-1])]
    if direction == 1: # West
        for row_index, row in enumerate(raw_data): # (no rotation, no reverse)
            new_data.append(tilt_row(row, row_index, True))
        
        return new_data
    if direction == 2: # South
        for column_index, column in enumerate(tuple([*zip(*raw_data)][::-1])): # (rotates left, reverse)
            new_data.append(tilt_row(column, column_index, False, True))
        
        return [*zip(*new_data[::-1])]
    else: # East
        for row_index, row in enumerate(raw_data): # (no rotation, reverse)
            new_data.append(tilt_row(row, row_index, True, True))
        
        return new_data


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
    else:
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


@cache
def tilt_OLD(data: tuple) -> tuple:
    row_amount, col_amount = (len(data), len(data[0]))
    column_heights_dict = {pos: 0 for pos in range(col_amount)}
    new_data = [['.' for _ in range(col_amount)] for _ in range(row_amount)]

    for vertical_position, row in enumerate(data):
        for horizontal_position, symbol in enumerate(row):
            if symbol == 'O':
                new_data[column_heights_dict[horizontal_position]][horizontal_position] = 'O'
                column_heights_dict[horizontal_position] += 1
            elif symbol == '#':
                new_data[vertical_position][horizontal_position] = '#'
                column_heights_dict[horizontal_position] = vertical_position + 1

    return new_data


def get_total_load(data: tuple) -> int:
    total_weight = 0

    load_value = len(data)
    for row in data:
        total_weight += row.count('O') * load_value
        load_value -= 1
    return total_weight


if __name__ == "__main__":
    main()
