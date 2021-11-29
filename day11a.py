with open('day11.txt') as f:
    lines = [list(line.rstrip()) for line in f]


def get_seat(row, col, grid):
    return grid[row][col]


# todo: change name
def check_seat(row, col, grid):
    max_row = len(grid)
    max_col = len(grid[0])
    changed = False

    if get_seat(row, col, grid) == ".":
        return

    if get_seat(row, col, grid) == "#":
        # check surroundings:
        if row + 1 is not max_row:
            if get_seat(row + 1, col, grid) == "L":
                grid[row + 1][col] = "#"




# def apply_rules(grid):
#     for row in lines:
#         for col in row:
#             # print(f"col: {col}")
#             if col == ".":
#                 continue
#             # if col == "L":
#
#
# apply_rules(lines)
check_seat(0, 0, lines)