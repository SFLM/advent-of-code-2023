with open("input.txt") as f:
    data_image = list(map(str.split, f.read().split('\n\n')))


def solver(data_map):
    for index in range(1, len(data_map)):
        # print(sum(top_symbol != bottom_symbol for top_row, bottom_row in zip(data_map[index:], data_map[index-1::-1]) for top_symbol,bottom_symbol in zip(top_row, bottom_row)))
        if sum(top_symbol != bottom_symbol for top_row, bottom_row in zip(data_map[index:], data_map[index-1::-1]) for top_symbol,bottom_symbol in zip(top_row, bottom_row)) == global_smudge_value:
            return index
    return 0


for global_smudge_value in 0,1:
    print(sum(100*solver(data_map) + solver([*zip(*data_map)]) for data_map in data_image))
