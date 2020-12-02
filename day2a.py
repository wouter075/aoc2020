from collections import Counter

with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]


def solve():
    good = 0
    for line in lines:
        parts = line.split(" ")
        password = parts[2]
        letter = parts[1].rstrip(":")
        l_min = int(parts[0].split("-")[0])
        l_max = int(parts[0].split("-")[1])

        ll = Counter(password)

        if ll[letter] in range(l_min, l_max + 1):
            good += 1
    print(f"Found: {good} matching passwords")


solve()
