def main():
    with open("example.txt") as f:
        pipe_map = f.read().splitlines()
    
    solution1(pipe_map)


def solution1(pipe_map):
    entry_point = get_entry_point(pipe_map)
    print(get_loop_length(pipe_map, entry_point))


def get_entry_point(pipe_map):
    for row_number, row in enumerate(pipe_map):
        for column_number, symbol in enumerate(row):
            if symbol == 'S':
                return (row_number, column_number)


def get_loop_length(pipe_map, starting_position, current_position = None, visited = None):
    directions_to_check = [True]*4 #Left, Right, Up, Down

    if current_position == starting_position:
        return len(visited)

    if not current_position:
        current_position = starting_position
        visited = [starting_position]
    
    # Check which directions are in range
    if current_position[1] == 0:
        directions_to_check[0] = False
    if current_position[1] == len(pipe_map[0])-1:
        directions_to_check[1] = False
    if current_position[0] == 0:
        directions_to_check[2] = False
    if current_position[0] == len(pipe_map):
        directions_to_check[3] = False
    
    x_position, y_position = current_position
    for direction_index, check_direction in enumerate(directions_to_check):
        if check_direction:
            match direction_index:
                case 0:
                    return "SDFSD"
                case 1:
                    return "Huh"
                case 2:
                    return "When"
                case _:
                    return "SDLKFKLSDF"


def is_accessible(pipe_map, from_position, to_position):
    pipe_dict = {
        '|': [False, False, True, True],
        '-': [True, True, False, False],
        'L': [False, True, True, False],
        'J': [True, False, True, False],
        'F': [False, True, False, True],
        '.': [False, False, False, False],
        'S': [True, True, True, True]
        }



if __name__ == "__main__":
    main()
