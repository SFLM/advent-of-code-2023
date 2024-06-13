def main():
    with open("example.txt") as f:
        data_image = f.read().splitlines()
    
    solution1(data_image)
    # solution2(data_image)


def solution1(data):
    expanded_universe = expand_universe(data)
    galaxies_dict = get_galaxies(expanded_universe)
    unprocessed_galaxies = [x for x in range(len(galaxies_dict))]
    total_distance = 0

    while unprocessed_galaxies:
        current_galaxy = unprocessed_galaxies.pop()
        for other_galaxy in unprocessed_galaxies:
            total_distance += abs(galaxies_dict[current_galaxy][0]-galaxies_dict[other_galaxy][0])
            total_distance += abs(galaxies_dict[current_galaxy][1]-galaxies_dict[other_galaxy][1])

    print(total_distance)


def expand_universe(data_image):
    expanded_universe = data_image
    height = len(data_image)
    width = len(data_image[0])
    expand_rows = set([x for x in range(height)])
    expand_columns = set([x for x in range(width)])

    galaxy_index = 0
    for row_number in range(height):
        for column_number in range(width):
            if data_image[row_number][column_number] == "#":
                expand_rows.discard(row_number)
                expand_columns.discard(column_number)

    for increment, row_to_expand in enumerate(expand_rows):
        expanded_universe.insert(row_to_expand+increment, 'M'*width)
    for row_index, row in enumerate(expanded_universe):
        updated_row = list(row)
        for increment, column_to_expand in enumerate(expand_columns):
            updated_row.insert(column_to_expand+increment, 'M')
        expanded_universe[row_index] = ''.join(updated_row)

    return expanded_universe


def get_galaxies(data_image):
    galaxies_dict = {}

    galaxy_index = 0
    for row_index, row in enumerate(data_image):
        for column_index, item in enumerate(row):
            if item == '#':
                galaxies_dict[galaxy_index] = (row_index, column_index)
                galaxy_index += 1
    
    return galaxies_dict

if __name__ == "__main__":
    main()
