with open('day6.txt') as f:
    data = f.read().split("\n\n")

answers = [line.replace("\n", " ") for line in data]
total = 0
for p in answers:
    parts = p.strip().split(" ")
    if len(parts) == 1:
        total += len(set(parts[0]))
    else:
        total += len(set.intersection(*map(set, parts)))

print(total)
