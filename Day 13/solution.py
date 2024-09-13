from functools import cache

def main():
    with open("input.txt") as f:
        data_image = f.read()
    
    print(f"Solution 1: {solution1(data_image)}")


def solution1(data_image: str) -> int:
    maps = parse_data(data_image)

    total = 0
    for map in maps:
        total += get_mirror_value(map)
    
    return total


def get_mirror_value(map: tuple) -> int:
    total = 0
    # Horizontal check
    horizontal_positions = []
    for row in map:
        horizontal_positions.append(get_mirror_position(row))
    
    # Vertical check
    vertical_positions = []
    for column_number in range(len(map[0])):
        positions = get_mirror_position(tuple(row[column_number] for row in map))
        vertical_positions.append(positions)
    
    for position in range(len(map[0]) - 1):
        if all(position in pos_set for pos_set in horizontal_positions):
            total += position + 1
            break

    for position in range(len(map) - 1):
        if all(position in pos_set for pos_set in vertical_positions):
            total += 100*(position + 1)
            break
    
    # print(f"Horizontals: {horizontal_positions}; Verticals: {vertical_positions}")

    return total


def get_mirror_position(series: tuple) -> int:
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


def parse_data(data_image: str) -> tuple:
    raw_maps = data_image.split("\n\n")

    maps = []
    for raw_map in raw_maps:
        maps.append(tuple(tuple(symbol for symbol in x) for x in raw_map.split('\n')))
    
    return tuple(maps)


if __name__ == "__main__":
    main()
