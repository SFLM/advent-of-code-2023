import re

def main():
    with open("input.txt") as f:
        input = re.split('(?> map)?:\s|\n+', f.read())
    
    solution1(input)
    solution2(input)

def solution1(information):
    seeds, map_dict = get_info(information)
    
    seed_index = 0
    while seed_index < len(seeds):
        for map_index in range(len(map_dict)):
            for map_line in map_dict[map_index]:
                if map_line[1] + map_line[2] >= seeds[seed_index] >= map_line[1]:
                    seeds[seed_index] += map_line[0] - map_line[1]
                    break
        seed_index += 1
    
    print(f"Solution 1: {min(seeds)}")

def solution2(information):
    seed_info, map_dict = get_info(information)
    unprocessed_ranges = [(seed_info[x], seed_info[x] + seed_info[x+1] - 1) for x in range(0, len(seed_info), 2)]
    processed_ranges = []

    for map_index in range(len(map_dict)):
        while unprocessed_ranges:
            current_range = unprocessed_ranges[-1]
            for map_line in map_dict[map_index]:
                overlap_info = get_overlap(current_range, map_line)
                if overlap_info:
                    unprocessed_ranges.pop()
                    processed_ranges.extend(overlap_info[0])
                    if overlap_info[1]:
                        unprocessed_ranges.extend(overlap_info[1])
                    break
            if unprocessed_ranges:
                if current_range == unprocessed_ranges[-1]:
                    processed_ranges.append(unprocessed_ranges.pop())
        processed_ranges, unprocessed_ranges = unprocessed_ranges, processed_ranges

    print(f"Solution 2: {sorted(unprocessed_ranges)[0][0]}")
                    


def get_info(information):
    seeds = [int(x) for x in information[1].split()]
    map_dict = {}
    map_dict_index = -1

    for line in information[2:]:
        if line[0].isnumeric():
            map_dict[map_dict_index].append([int(x) for x in line.split()])
        else:
            map_dict_index += 1
            map_dict[map_dict_index] = []
    
    return seeds, map_dict

def get_overlap(seed_range, instruction):
    range_min, range_max = seed_range
    instruction_min = instruction[1]
    instruction_max = instruction[1] + instruction[2] - 1
    instruction_modifier = instruction[0] - instruction[1]

    # Inner overlap
    if instruction_min <= range_min and range_max <= instruction_max:
        return ([(range_min + instruction_modifier, range_max + instruction_modifier)], None)
    
    # Left overlap
    if range_min < instruction_min <= range_max <= instruction_max:
        return ([(instruction_min + instruction_modifier, range_max + instruction_modifier)], [(range_min, instruction_min - 1)])
    
    # Right overlap
    if instruction_min <= range_min <= instruction_max < range_max:
        return ([(range_min + instruction_modifier, instruction_max + instruction_modifier)], [(instruction_max + 1, range_max)])
    
    # Outer overlap
    if range_min < instruction_min and instruction_max < range_max:
        return ([(instruction_min + instruction_modifier, instruction_max + instruction_modifier)], [(range_min, instruction_min - 1), (instruction_max + 1, range_max)])
    
    # No overlap
    return False

if __name__ == "__main__":
    main()