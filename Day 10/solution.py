PIPE_DICT = {
        '|': [False, False, True, True], # Left, Right, Up, Down
        '-': [True, True, False, False],
        'L': [False, True, True, False],
        'J': [True, False, True, False],
        '7': [True, False, False, True],
        'F': [False, True, False, True],
        '.': [False, False, False, False],
        'S': [True, True, True, True]
        }

PIPE_MAP = None


def main():
    with open("input.txt") as f:
        global PIPE_MAP
        PIPE_MAP = f.read().splitlines()
    
    entry_point = get_entry_point()
    solution1(entry_point)
    solution2(entry_point)


def solution1(entry_point):
    print(f"Solution 1: {loop_info(entry_point)['solution_1']}")


def solution2(entry_point):
    info = loop_info(entry_point)
    print(f"Solution 2: {flood_fill_algo(info['start_opening_directions'], info['explored_path'])}")


def get_entry_point():
    for row_number, row in enumerate(PIPE_MAP):
        for column_number, symbol in enumerate(row):
            if symbol == 'S':
                return (row_number, column_number)


def loop_info(start_position):
    explored_path = set()
    current_position = start_position
    last_position_direction = None
    start_position_pipe_opening = None

    while current_position != start_position or len(explored_path) == 0:
        # Check which directions are in range
        directions_to_check = [True]*4 #Left, Right, Up, Down
        if last_position_direction != None:
            directions_to_check[last_position_direction] = False
        if current_position[1] == 0:
            directions_to_check[0] = False
        if current_position[1] == len(PIPE_MAP[0])-1:
            directions_to_check[1] = False
        if current_position[0] == 0:
            directions_to_check[2] = False
        if current_position[0] == len(PIPE_MAP):
            directions_to_check[3] = False
        
        for direction_index, do_check in enumerate(directions_to_check):
            if do_check:
                next_pipe = is_accessible(current_position, direction_index)
                if next_pipe:
                    if not start_position_pipe_opening:
                        start_position_pipe_opening = direction_index
                    if direction_index % 2 == 0:
                        last_position_direction = direction_index+1
                    else:
                        last_position_direction = direction_index-1
                    current_position = next_pipe
                    explored_path.add(next_pipe)
                    break
    
    start_pipe_direction_openings = [False]*4
    start_pipe_direction_openings[start_position_pipe_opening] = True
    start_pipe_direction_openings[last_position_direction] = True
    return {"solution_1": int(len(explored_path)/2), "explored_path": explored_path, "start_opening_directions": start_pipe_direction_openings}


def flood_fill_algo(start_pipe_openings, loop_path):
    side1_tiles = 0
    side2_tiles = 0
    first_side = True
    for row_position, row in enumerate(PIPE_MAP):
        for col_position, tile in enumerate(row):
            if (row_position, col_position) in loop_path:
                if tile == 'S':
                    if start_pipe_openings[3]:
                        first_side = not first_side
                elif PIPE_DICT[tile][3]:
                    first_side = not first_side
            else:
                if first_side:
                    side1_tiles += 1
                else:
                    side2_tiles += 1
    
    return (side1_tiles, side2_tiles)


def is_accessible(from_position, direction):
    from_row, from_column = from_position
    from_pipe = PIPE_MAP[from_row][from_column]
    if PIPE_DICT[from_pipe][direction]:
        if direction == 0:
            to_pipe = PIPE_MAP[from_row][from_column-1]
            if PIPE_DICT[to_pipe][direction+1]:
                return (from_row, from_column-1)
        elif direction == 1:
            to_pipe = PIPE_MAP[from_row][from_column+1]
            if PIPE_DICT[to_pipe][direction-1]:
                return (from_row, from_column+1)
        elif direction == 2:
            to_pipe = PIPE_MAP[from_row-1][from_column]
            if PIPE_DICT[to_pipe][direction+1]:
                return (from_row-1, from_column)
        elif direction == 3:
            to_pipe = PIPE_MAP[from_row+1][from_column]
            if PIPE_DICT[to_pipe][direction-1]:
                return (from_row+1, from_column)
    return False



if __name__ == "__main__":
    main()
