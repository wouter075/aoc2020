with open('day9.txt') as f:
    lines = [int(line.rstrip()) for line in f]


def solve(preamble):
    c = 0
    for l in range(preamble, len(lines)):
        found = False
        s = lines[l]
        for x in range(c, preamble):
            for y in range(c, preamble):
                if x == y:
                    continue
                if s == lines[x] + lines[y]:
                    found = True
                    break

        if not found:
            return s
        c += 1
        preamble += 1


# print(solve(25))
