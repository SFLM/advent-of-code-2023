from functools import cache
from typing import Union
import time

CUBE_LOCATIONS = dict()
PATTERNS = dict()

def main():

    with open("input.txt") as f:
        data = tuple(f.read())
    
    solution1(data)
    # solution2(data)


def solution1(data: tuple) -> None:
    print(data)


def solution2(data: tuple) -> None:
    pass


if __name__ == "__main__":
    main()
