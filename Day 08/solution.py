from math import lcm


def main():
    with open("input.txt") as f:
        instructions = f.readline().strip()
        map = f.read().splitlines()[1:]
    map_dict = generate_dict(map)

    solution1(map_dict, instructions)
    solution2(map_dict, instructions)


def solution1(map_dict, instructions):    
    steps = 0
    node = "AAA"
    while node != "ZZZ":
        direction = instructions[steps % len(instructions)]
        if direction == 'L':
            node = map_dict[node][0]
        else:
            node = map_dict[node][1]
        steps += 1

    print(f"Solution 1: {steps}")


def solution2(map_dict, instructions):
    steps = 0
    nodes = get_starting_nodes(map_dict)
    steps_needed = []
    direction_value = -1
    while nodes:
        new_nodes = []
        direction = instructions[steps % len(instructions)]
        direction_value = 0 if direction == 'L' else 1
        for node in nodes:
            if node[-1] == 'Z':
                steps_needed.append(steps)
            else:
                new_nodes.append(map_dict[node][direction_value])
        nodes = new_nodes
        steps += 1

    print(f"Solution 2: {lcm(*steps_needed)}")


def all_nodes_at_destination(nodes):
    for node in nodes:
        if node[-1] != 'Z':
            return False
    return True


def get_starting_nodes(map_dict):
    keys = []
    for key in map_dict.keys():
        if key[-1] == 'A':
            keys.append(key)

    return keys


def generate_dict(map):
    generated_dict = {}
    for item in map:
        node, paths = item.split(' = ')
        left_path, right_path = paths.strip('()').split(', ')
        generated_dict[node] = (left_path, right_path)

    return generated_dict


if __name__ == "__main__":
    main()
