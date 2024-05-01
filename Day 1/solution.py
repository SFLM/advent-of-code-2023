def main():
    with open("input.txt") as f:
        document = f.read().splitlines()
    
    solution1(document)
    solution2(document)


def solution1(document):
    calibration_values = []
    left, right = [], []
    for line in document:
        left_right_values = get_digits(line)
        left.append(left_right_values[0])
        right.append(left_right_values[1])
        calibration_values.append(combined_number(left, right))
        left, right = [], []
    
    print(f"Solution 1: {sum(calibration_values)}")


def solution2(document):
    calibration_values = []
    left, right = [], []
    for line in document:
        left_right_values = get_digits(line)
        left.append(left_right_values[0])
        right.append(left_right_values[1])
        additional_left_right_values = get_spelled_digits(line)
        left.append(additional_left_right_values[0])
        right.append(additional_left_right_values[1])
        calibration_values.append(combined_number(left, right))
        left, right = [], []
    
    print(f"Solution 2: {sum(calibration_values)}")


def get_digits(document_line):
    left_digit = (0, float("inf"))
    right_digit = (0, -1)
    for index, symbol in enumerate(document_line):
        if symbol.isdigit():
            left_digit = (symbol, index)
            break
    for index, symbol in enumerate(reversed(document_line)):
        if symbol.isdigit():
            right_digit = (symbol, len(document_line)-index-1)
            break
    return left_digit, right_digit


def get_spelled_digits(document_line):
    left_digit = (0, float("inf"))
    right_digit = (0, -1)
    spelled_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit_value, spelled_digit in enumerate(spelled_digits, 1):
        left_digit_index = document_line.find(spelled_digit)
        if left_digit_index != -1 and left_digit_index < left_digit[1]:
            left_digit = (digit_value, left_digit_index)
        right_digit_index = document_line.rfind(spelled_digit)
        if left_digit_index != -1 and right_digit_index > right_digit[1]:
            right_digit = (digit_value, right_digit_index)
    
    return left_digit, right_digit


def combined_number(left_digit_tuples, right_digit_tuples):
    left_symbol = min(left_digit_tuples, key = lambda x:x[1])[0]
    right_symbol = max(right_digit_tuples, key = lambda x:x[1])[0]
    return int(f"{left_symbol}{right_symbol}")


if __name__ == "__main__":
    main()


# Legacy version (not a robust solution and also looks very ugly)

# spelled_digits = [
#     "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
# ]

# total = 0
# with open("input.txt") as file:
#     for line in file:
#         first_number = None
#         first_number_index = -1
#         last_number = None
#         last_number_index = float("inf")
#         # print(f"Looking through {line}")
#         for real_digit, spelled_digit in enumerate(spelled_digits, 1):
#             left_digit_index = line.find(spelled_digit)
#             right_digit_index = line.rfind(spelled_digit)
#             if left_digit_index != -1:
#                 # print(f"Found {spelled_digit} at index {left_digit_index}")
#                 if (not first_number) or (left_digit_index < first_number_index):
#                     # print(f"Setting first number to {real_digit}")
#                     first_number = real_digit
#                     first_number_index = left_digit_index
#                 if (not last_number) or (right_digit_index > last_number_index):
#                     # print(f"Setting last number to {real_digit}")
#                     last_number = real_digit
#                     last_number_index = right_digit_index
#         # print("Now looking for digits in string")
#         for char_index, char in enumerate(line):
#             if char.isdigit():
#                 # print(f"Found {char} at index {char_index}")
#                 if (not first_number) or (char_index < first_number_index):
#                     # print(f"Setting first number to {char}")
#                     first_number = char
#                     first_number_index = char_index
#                 if (not last_number) or (char_index > last_number_index):
#                     # print(f"Setting last number to {char}")
#                     last_number = char
#                     last_number_index = char_index
#         # print(f"Adding to total: {first_number}{last_number}\n\n")
#         total += int(f"{first_number}{last_number}")

# print(f"Total: {total}")