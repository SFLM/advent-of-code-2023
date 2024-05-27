def main():
    with open("input.txt") as f:
        lines = f.readlines()

    lines = [line.rstrip() for line in lines]

    solution1(lines)
    solution2(lines)

def solution1(lines):
    total = 0
    for line_index, line in enumerate(lines):
        line_position = 0
        for spot in line:
            if spot != "." and not spot.isnumeric():
                line = line.replace(spot, ".")
        items = [x for x in line.split(".") if x]
        for item in items:
            item_x_pos = line.find(item, line_position)
            line_position = item_x_pos + len(item)
            surrounding_lines = []
            surrounding_lines.append(lines[line_index])
            if line_index > 0:
                surrounding_lines.append(lines[line_index - 1])
            if line_index < len(lines) - 1:
                surrounding_lines.append(lines[line_index + 1])

            total += return_if_part_number(item, item_x_pos, surrounding_lines, len(line))

    print(f"Solution 1: {total}")

def solution2(lines):
    total = 0
    wheels = []
    numbers = []
    for y_position, line in enumerate(lines):
        line_position = 0
        for x_position, spot in enumerate(line):
            if spot != "." and not spot.isnumeric():
                if spot == "*":
                    wheels.append((x_position, y_position))
                line = line.replace(spot, ".")
        raw_numbers = [x for x in line.split(".") if x]
        for number in raw_numbers:
            number_x_pos = line.find(number, line_position)
            line_position = number_x_pos + len(number)
            numbers.append((number_x_pos, y_position, number))

    for wheel in wheels:
        adjacent_numbers = []
        surrounding_numbers = [x for x in numbers if -1 <= x[1] - wheel[1] <= 1]
        range_left = wheel[0] - 1
        range_right = wheel[0] + 2
        if wheel[0] == 0:
            range_left = 0
        if wheel[0] == len(line) - 1:
            range_right = len(line)
        for surrounding_number in surrounding_numbers:
            for x in range(range_left, range_right):
                if x in range(surrounding_number[0], surrounding_number[0] + len(surrounding_number[2])):
                    adjacent_numbers.append(int(surrounding_number[2]))
                    break

        if len(adjacent_numbers) == 2:
            total += adjacent_numbers[0]*adjacent_numbers[1]

    print(f"Solution 2: {total}")

def return_if_part_number(item, item_position, surrounding_lines, line_length):    
    range_start = item_position - 1
    range_end = item_position + len(item) + 1
    if item_position == 0:
        range_start = 0
    if item_position + len(item) == line_length:
        range_end = item_position + len(item)
    item_occupied_space = range(range_start, range_end)

    for spot in item_occupied_space:
        for line in surrounding_lines:
            if line[spot] != "." and not line[spot].isnumeric():
                return int(item)
    return 0

if __name__ == "__main__":
    main()