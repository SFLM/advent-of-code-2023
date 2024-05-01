def main():
    with open("input.txt") as f:
        # For every line, split on whitespace and convert the second element to an int [string, int]
        input = [(lambda x: [x[0], int(x[1])])(y.split()) for y in f]
    
    solution1(input)
    solution2(input)

def solution1(input):
    process_hands(input)

def solution2(input):
    process_hands(input, part=2)

def process_hands(input, part=1):
    hands_info = []
    winnings = 0
    
    hand_cards = {}
    for hand_and_bid in input:
        hand, bid = hand_and_bid

        for card in hand:
            if card in hand_cards:
                hand_cards[card] += 1
            else:
                hand_cards[card] = 1
        hands_info.append([get_type(hand_cards, part)] + get_card_strengths(hand, part) + [hand, bid])
        hand_cards = {}

    for rank, info in enumerate(sorted(hands_info), 1):
        winnings += info[-1]*rank

    print(f"Solution {part}: {winnings}")

def get_type(hand_amounts, part=1):
    if part == 2:
        if 'J' in hand_amounts and len(hand_amounts) > 1:
            jonker = hand_amounts.pop('J')
            hand_amounts[max(hand_amounts, key=hand_amounts.get)] += jonker

    highest_combo = max(hand_amounts.values())
    unique_count = len(hand_amounts)
    match unique_count:
        case 1:
            return 7
        case 2 if highest_combo == 4:
            return 6
        case 2:
            return 5
        case 3 if highest_combo == 3:
            return 4
        case 3:
            return 3
        case 4:
            return 2
        case _:
            return 1

def get_card_strengths(hand, part=1):
    if part == 1:
        card_strengths = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
    else:
        card_strengths = {'J': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'Q': 11, 'K': 12, 'A': 13}
    hand_strengths = []

    for card in hand:
        hand_strengths.append(card_strengths[card[0]])
    
    return hand_strengths

if __name__ == "__main__":
    main()