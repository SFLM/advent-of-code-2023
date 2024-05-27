import re

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    lines = [x.rstrip() for x in lines]

    solution1(lines)
    solution2(lines)

def solution1(lines):
    total = 0
    cards = [x.split(':')[1] for x in lines]
    for card in cards:
        elf_numbers = re.split(' +', card.split('|')[1])
        winning_numbers = re.split(' +', card.split('|')[0].strip())
        matches = match_amount(elf_numbers, winning_numbers)
        if matches != 0:
            total += int(2**matches/2)
        
    print(f"Solution 1: {total}")

# Challenged myself to write this in as little lines as possible, don't do this, this is really really bad
def solution2(lines):
    print("Solution 2: " + str(recursive_solver({int(re.split(' +', x.split(':')[0])[1]): {'matches': match_amount(re.split(' +', x.split(':')[1].split('|')[1]), re.split(' +', x.split(':')[1].split('|')[0].strip())), 'amount': 1} for x in lines})))

def recursive_solver(card_dict, start = 1):
    if start == len(card_dict) + 1:
        return get_total_cards(card_dict)
    for card_number in range(start, len(card_dict) + 1):
        for i in range(card_number + 1, card_number + card_dict[card_number]["matches"] + 1):
            card_dict[i]["amount"] += card_dict[card_number]["amount"]
        return recursive_solver(card_dict, start+1)

def get_total_cards(card_dict):
    total = 0
    if len(card_dict) == 0:
        return 0
    for card_index in range(1, len(card_dict)+1):
        total += card_dict[card_index]["amount"]
    return total

def match_amount(elf_numbers, winning_numbers):
    matches = 0
    for elf_number in elf_numbers:
        if elf_number in winning_numbers:
            matches += 1
    return matches

if __name__ == "__main__":
    main()