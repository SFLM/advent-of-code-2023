def main():
    with open("input.txt") as f:
        data_image = f.read().splitlines()
    
    expanded_universe = expand_universe(data_image)
    galaxies_dict = get_galaxies(expanded_universe)
    
    solution1(expanded_universe, galaxies_dict)
    solution2(expanded_universe, galaxies_dict)


def solution1(data, galaxies):
    print(f"Solution 1: {get_total_distance(data, galaxies)}")


def solution2(data, galaxies):
    print(f"Solution 2: {get_total_distance(data, galaxies, old_galaxies=True)}")


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


def get_total_distance(data_image, galaxies_dict, old_galaxies=False):
    OLD_GALAXY_DISTANCE = 999999
    unprocessed_galaxies = [x for x in range(len(galaxies_dict))]
    total_distance = 0

    while unprocessed_galaxies:
        current_galaxy = unprocessed_galaxies.pop()
        for other_galaxy in unprocessed_galaxies:
            vertical_matrix_delta = abs(galaxies_dict[current_galaxy][0]-galaxies_dict[other_galaxy][0])
            horizontal_matrix_delta = abs(galaxies_dict[current_galaxy][1]-galaxies_dict[other_galaxy][1])
            if old_galaxies:
                for row_iteration in range(vertical_matrix_delta):
                    if galaxies_dict[current_galaxy][0] == galaxies_dict[other_galaxy][0]:
                        continue
                    elif galaxies_dict[current_galaxy][0] > galaxies_dict[other_galaxy][0]:
                        row_iteration = -row_iteration
                    if all(x=='M' for x in data_image[galaxies_dict[current_galaxy][0] + row_iteration]):
                        total_distance += OLD_GALAXY_DISTANCE
                    else:
                        total_distance += 1
                for column_iteration in range(horizontal_matrix_delta):
                    if galaxies_dict[current_galaxy][1] == galaxies_dict[other_galaxy][1]:
                        continue
                    elif galaxies_dict[current_galaxy][1] > galaxies_dict[other_galaxy][1]:
                        column_iteration = -column_iteration
                    if data_image[galaxies_dict[current_galaxy][0]][galaxies_dict[current_galaxy][1] + column_iteration] == 'M':
                        total_distance += OLD_GALAXY_DISTANCE
                    else:
                        total_distance += 1
            else:
                total_distance += vertical_matrix_delta + horizontal_matrix_delta
    
    return total_distance



if __name__ == "__main__":
    main()
