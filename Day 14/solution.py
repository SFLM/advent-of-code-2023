from functools import cache

def main():

    with open("example.txt") as f:
        data = tuple(f.read().splitlines())
    
    solution1(data)
    solution2(data)


def solution1(data: tuple) -> None:
    tilted_data = tilt(data)
    print(f"Solution 1: {get_total_load(tilted_data)}")


def solution2(data) -> None:
    tilted_data = tilt(data)
    rotations = 3
    while rotations - .25 > 0:
        tilted_data = tilt(tuple([*zip(*reversed(tilted_data))]))
        rotations -= .25

    tilted_data = tuple([*zip(*reversed(tilted_data))])

    for r in tilted_data:
        print(''.join(r))

    print(f"Solution 2: {get_total_load(tilted_data)}")


@cache
def tilt(data: tuple) -> tuple:
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
