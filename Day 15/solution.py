import re

def main():

    with open("input.txt") as f:
        data = f.read().split(',')
    
    solution1(data)
    solution2(data)


def solution1(sequence: list) -> None:
    total = 0
    for step in sequence:
        total += process_step(step)
    
    print(f"Solution 1: {total}")


def solution2(sequence: list) -> None:
    boxes = [Box() for _ in range(256)]
    for step in sequence:
        label, modifier = re.split("(?=[=-])", step)
        box_number = process_step(label)
        if modifier[0] == '-':
            boxes[box_number].remove_lens(label)
        else:
            new_lens = Lens(label, int(modifier[1:]))
            boxes[box_number].add_lens(new_lens)


    print(f"Solution 2: {get_focusing_power(boxes)}")


def process_step(step: str) -> int:
    current_value = 0
    for character in step:
        current_value += ord(character)
        current_value *= 17
        current_value %= 256

    return current_value


def get_focusing_power(box_collection: list) -> int:
    focusing_power = 0
    for box_number, box in enumerate(box_collection):
        for lens_number, lens in enumerate(box.get_lenses()):
            focusing_power += (box_number + 1) * (lens_number + 1) * lens.get_focal_length()
    
    return focusing_power


class Lens:
    def __init__(self, label: str, focal_length: int):
        self.label = label
        self.focal_length = focal_length
    
    def get_label(self):
        return self.label

    def get_focal_length(self):
        return self.focal_length
    
    def __repr__(self):
        return self.label


class Box:
    def __init__(self):
        self.lenses = []
    
    def remove_lens(self, label):
        for index, lens in enumerate(self.lenses):
            if lens.get_label() == label:
                del self.lenses[index]
                break
    
    def add_lens(self, lens: Lens):
        for index, own_lens in enumerate(self.lenses):
            if own_lens.get_label() == lens.get_label():
                self.lenses[index] = lens
                return
        
        self.lenses.append(lens)
    
    def get_lenses(self):
        return self.lenses
    
    def __repr__(self):
        return str(self.lenses)


if __name__ == "__main__":
    main()
