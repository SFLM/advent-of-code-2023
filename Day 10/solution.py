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
    with open("example2.txt") as f:
        global PIPE_MAP
        PIPE_MAP = f.read().splitlines()
    
    solution1()


def solution1():
    entry_point = get_entry_point()
    print(f"Solution 1: {get_loop_length(entry_point)}")


def get_entry_point():
    for row_number, row in enumerate(PIPE_MAP):
        for column_number, symbol in enumerate(row):
            if symbol == 'S':
                return (row_number, column_number)


def get_loop_length(start_position, current_position=None, last_position_direction=None, current_length=0):
    if current_position == start_position:
        return current_length
        
    if current_position == None:
        current_position = start_position
    
    current_length += 1

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
                if direction_index % 2 == 0:
                    receiving_direction = direction_index+1
                else:
                    receiving_direction = direction_index-1
                return get_loop_length(start_position, next_pipe, receiving_direction, current_length)
    
    return current_length/2

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
