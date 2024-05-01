spelled_digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]

total = 0
with open("input.txt") as file:
    for line in file:
        first_number = None
        first_number_index = -1
        last_number = None
        last_number_index = float("inf")
        # print(f"Looking through {line}")
        for real_digit, spelled_digit in enumerate(spelled_digits, 1):
            left_digit_index = line.find(spelled_digit)
            right_digit_index = line.rfind(spelled_digit)
            if left_digit_index != -1:
                # print(f"Found {spelled_digit} at index {left_digit_index}")
                if (not first_number) or (left_digit_index < first_number_index):
                    # print(f"Setting first number to {real_digit}")
                    first_number = real_digit
                    first_number_index = left_digit_index
                if (not last_number) or (right_digit_index > last_number_index):
                    # print(f"Setting last number to {real_digit}")
                    last_number = real_digit
                    last_number_index = right_digit_index
        # print("Now looking for digits in string")
        for char_index, char in enumerate(line):
            if char.isdigit():
                # print(f"Found {char} at index {char_index}")
                if (not first_number) or (char_index < first_number_index):
                    # print(f"Setting first number to {char}")
                    first_number = char
                    first_number_index = char_index
                if (not last_number) or (char_index > last_number_index):
                    # print(f"Setting last number to {char}")
                    last_number = char
                    last_number_index = char_index
        # print(f"Adding to total: {first_number}{last_number}\n\n")
        total += int(f"{first_number}{last_number}")

print(f"Total: {total}")