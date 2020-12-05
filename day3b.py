with open("day3.txt") as file:
    lines = [line.strip() for line in file]

tree = 0
counter = 0
right = 0
row = 0

encounters = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
total = 1

for e in encounters:
    for line in lines:
        line = list(line)
        if counter % e[1] == e[1] - 1:
            if line[right] == "#":
                tree += 1

        counter += 1
        right += e[0]
        row += e[1]

        if right >= len(line):
            right = right % len(line)
    row = 0
    right = 0
    counter = 0
    total = total * tree
    tree = 0
print(total)
