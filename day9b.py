from day9a import solve

with open('day9.txt') as f:
    lines = [int(line.rstrip()) for line in f]


anwser = solve(25)
m = lines.index(anwser)


def summon(start, end):
    t = 0
    for s in range(start, end):
        t += lines[s]
    return t


def extract(start, end):
    t = []
    for s in range(start, end):
        t.append(lines[s])
    return min(t) + max(t)


for x in range(0, m):
    for y in range(0, m):
        if x == y:
            continue
        if anwser == summon(x, y):
            print(extract(x, y))
            break




