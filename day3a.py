with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

tree = 0
right = 0
down = 0
counter = 0
for line in lines:
    line = list(line)
    # print(right)
    if counter is not 0:
        if line[right] == "#":
            # line[right] = "X"
            tree += 1
        # else:
        #     line[right] = "O"

    down += 1
    right += 3
    if right >= len(line):
        right = right % len(line)

    # print("".join(line))
    counter += 1
print(f"Argghhh we just hit {tree} trees!")