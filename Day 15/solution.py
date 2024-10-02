def main():

    with open("input.txt") as f:
        data = f.read().split(',')
    
    solution1(data)
    # solution2(data)


def solution1(sequence: list) -> None:
    total = 0
    for step in sequence:
        total += process_step(step)
    
    print(f"Solution 1: {total}")


def solution2(data: tuple) -> None:
    pass


def process_step(step: str) -> int:
    current_value = 0
    for character in step:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256

    return current_value


if __name__ == "__main__":
    main()
