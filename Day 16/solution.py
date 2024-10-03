def main():

    with open("example.txt") as f:
        data = f.read().splitlines()
    
    solution1(data)
    # solution2(data)


def solution1(data) -> None:
    print(data)


def solution2(data) -> None:
    pass


if __name__ == "__main__":
    main()
