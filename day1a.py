with open('day1.txt') as f:
    lines = [int(line.rstrip()) for line in f]


def solve():
    for l1 in lines:
        for l2 in lines:
            if l1 + l2 == 2020:
                print(f"Found: {l1} + {l2} = 2020 -> {l1 * l2}")
                return


solve()
