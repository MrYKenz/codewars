def validate_battlefield(field):
    # connected-component labeling 
    ships = {}
    for row in range(len(field)):
        for col in range(len(field)):
            if field[row][col] == 1: # not background
                try:
                    result = ship_size(row, col, field)
                    ships[result] = ships.get(result, 0) + 1
                except ValueError:
                    return False
    return sum(ships.get(5-x, 0) == x for x in range(1,5)) == 4


def corner_valid(row, col, field):
    if row == len(field) - 1:
        return True
    if col == 0:
        return field[row + 1][col + 1] != 1
    if col == len(field[0]) - 1:
        return field[row + 1][col - 1] != 1
    return field[row + 1][col + 1] != 1 and field[row + 1][col - 1] != 1


def side_valid(row, col, field):
    if row == len(field) - 1 or col == len(field[0]) - 1:
        return True
    return not(field[row + 1][col] != 0 and field[row][col + 1] != 0)


def ship_size(row, col, field):
    if not(side_valid(row, col, field) and corner_valid(row, col, field)):
        raise ValueError('Invalid disposition')
    field[row][col] = -1
    if row != 9 and field[row + 1][col] == 1:
        return 1 + ship_size(row + 1, col, field)
    if col != 9 and field[row][col + 1] == 1:
        return 1 + ship_size(row, col + 1, field)
    return 1

print(validate_battlefield(
                [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
