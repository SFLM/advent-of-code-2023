colors = ["red", "green", "blue"]
all_games_info = []
RED, GREEN, BLUE = 12, 13, 14

def main():
    read_input("input.txt")
    print(f"Solution 1: {get_solution1(RED, GREEN, BLUE)}")
    print(f"Solution 2: {get_solution2()}")

def read_input(file_name):
    with open(file_name) as f:
        for line in f:
            all_games_info.append(get_game_info(line))

def get_rgb_maxes(game_line):
    maxes = [0, 0, 0]
    part = game_line.split(": ")
    turns = part[1].split("; ")
    for turn in turns:
        turn_info = turn.split(", ")
        for amount_and_color in turn_info:
            color_index = colors.index(amount_and_color.split(" ")[1])
            amount = int(amount_and_color.split(" ")[0])
            if amount > maxes[color_index]:
                maxes[color_index] = amount
    return maxes

def get_game_id(game_line):
    part = game_line.split(": ")
    result = part[0].split(" ")
    return int(result[1])

def get_game_info(game_line):
    return [get_game_id(game_line.rstrip())] + get_rgb_maxes(game_line.rstrip())

def get_solution1(red, green, blue):
    total = 0
    for game_info in all_games_info:
        if game_info[1] <= red and game_info[2] <= green and game_info[3] <= blue:
            total += game_info[0]
    return total

def get_solution2():
    total = 0
    for game_info in all_games_info:
        total += game_info[1] * game_info[2] * game_info[3]
    return total

if __name__ == "__main__":
    main()