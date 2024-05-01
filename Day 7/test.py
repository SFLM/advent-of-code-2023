cool_dict = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
jonker = cool_dict.pop('J')
print(f"Jonker: {jonker}")
print(cool_dict)
print(max(cool_dict, key=cool_dict.get))