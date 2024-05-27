import math
from time import perf_counter

def main():
    with open("input.txt") as f:
        input = f.read()
    
    race_time, distance_to_beat = parse_input_2(input)
    literally_empty()
    solution1(parse_input_1(input))
    quadratic(parse_input_2(input))
    binary(race_time, distance_to_beat, 0)
    brute_force(parse_input_2(input))

def solution1(input):
    start_time = perf_counter()
    times, distances = input
    wins = [0] * len(times)
    
    for race_id, race_time in enumerate(times):
        for press_time in range(1, race_time):
            local_distance = (race_time - press_time) * press_time
            if local_distance > distances[race_id]:
                wins[race_id] += 1
    
    print(f"Solution 1: {math.prod(wins)}, operation took {perf_counter() - start_time:.6f} seconds")

def literally_empty():
    start_time = perf_counter()
    print(f"Empty method, operation took {perf_counter() - start_time:.6f} seconds")

def quadratic(input):
    start_time = perf_counter()
    time, distance = input
    # Quadratic formula lmao, reasoning in math.txt
    minimum = (-time+math.sqrt(time**2-4*distance))/-2

    print(f"Quadratic: {time-2*math.ceil(minimum)+1}, operation took {perf_counter() - start_time:.6f} seconds")

# Scuffed binary search method
def binary(race_time, distance_to_beat, left):
    start_time = perf_counter()
    range_left = recursive_binary_search(race_time, distance_to_beat, left, race_time//2)

    print(f"Binary: {race_time-2*range_left+1}, operation took {perf_counter() - start_time:.6f} seconds")

def recursive_binary_search(race_time, distance_to_beat, left, right):
    mid = (left + right) // 2
    if mid == left or mid == right:
        if (race_time - left) * left > distance_to_beat and (race_time - (left-1)) * (left-1) < distance_to_beat:
            return left
        else:
            return right
    if (((race_time - mid) * mid > distance_to_beat != (race_time - (mid+1)) * (mid+1) < distance_to_beat) or
        ((race_time - mid) * mid > distance_to_beat != (race_time - (mid-1)) * (mid-1) < distance_to_beat)):
        return mid
    else:
        if (race_time - left) * left < distance_to_beat and (race_time - (mid-1)) * (mid-1) > distance_to_beat:
            return recursive_binary_search(race_time, distance_to_beat, left, mid-1)
        else:
            return recursive_binary_search(race_time, distance_to_beat, mid+1, right)

# Pain
def brute_force(input):
    start_time = perf_counter()
    race_time, distance_to_beat = input
    wins = 0
    faster = False
    
    for press_time in range(1, race_time):
        local_distance = (race_time - press_time) * press_time
        if faster:
            if local_distance < distance_to_beat:
                break
        if local_distance > distance_to_beat:
            wins += 1
            if not faster:
                faster = True

    print(f"Brute-force: {wins}, operation took {perf_counter() - start_time:.6f} seconds")

def parse_input_1(input):
    return [[int(x) for x in y.split()[1:]] for y in input.split('\n')]

def parse_input_2(input):
    return [int(''.join([str(x) for x in y])) for y in parse_input_1(input)]

if __name__ == "__main__":
    main()