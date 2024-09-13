from functools import cache
from copy import deepcopy

def main():
    with open("input.txt") as f:
        data_image = f.read()
    
    print(f"Solution 1: {solution1(data_image)}")
    print(f"Solution 2: {solution2(data_image)}")


def solution1(data_image: str) -> int:
    maps = parse_data(data_image)

    total = 0
    for map in maps:
        val = get_mirror_value(map)
        total += val
    
    return total


def solution2(data_image: str) -> int:
    maps = parse_data(data_image)

    total = 0
    for map in maps:
        val = get_smudged_value(map)
        total += val
    
    return total

def get_smudged_value(map: list, row_position: int = 0, column_position: int = 0) -> int:
    column_length = len(map)
    row_length = len(map[0])
    for row_index in range(column_length):
        for column_index in range(row_length):
            changed_map = deepcopy(map)
            symbol = map[row_position][column_position]
            if symbol == '#':
                new_symbol = '.'
            else:
                new_symbol = '#'
            changed_map[row_index][column_index] = new_symbol

            original_value = get_mirror_value(map)

            changed_value = get_mirror_value(changed_map, original_value)

            if changed_value != 0 and original_value != changed_value:
                return changed_value

    return original_value


def get_mirror_value(map: list, original_value: int = -1) -> int:
    total = 0
    # Horizontal check
    horizontal_positions = []
    for row in map:
        horizontal_positions.append(get_mirror_positions(row))
    
    # Vertical check
    vertical_positions = []
    for column_number in range(len(map[0])):
        positions = get_mirror_positions(tuple(row[column_number] for row in map))
        vertical_positions.append(positions)
    
    
    for position in range(len(map) - 1):
        if all(position in pos_set for pos_set in vertical_positions):
            total += 100*(position + 1)
            if total == original_value:
                total = 0
            else:
                if total != 0:
                    return total
                break
    for position in range(len(map[0]) - 1):
        if all(position in pos_set for pos_set in horizontal_positions):
            total += position + 1
            if total == original_value:
                total = 0
            else:
                if total != 0:
                    return total
                break
    
    # print(f"Horizontals: {horizontal_positions}; Verticals: {vertical_positions}")
    return total


def get_mirror_positions(series: tuple) -> int:
    possible_locations = set()
    for depth in range(len(series) - 1):
        if check_mirrored(series, depth):
            possible_locations.add(depth)
    return possible_locations


def check_mirrored(series: tuple, position: int) -> bool:
    for depth in range(position + 1):
        if position + depth + 1 == len(series):
            return True
        if series[position - depth] != series[position + depth + 1]:
            return False
    return True


def parse_data(data_image: str) -> list:
    raw_maps = data_image.split("\n\n")

    maps = []
    for raw_map in raw_maps:
        maps.append([[symbol for symbol in x] for x in raw_map.split('\n')])
    
    return maps


if __name__ == "__main__":
    main()
