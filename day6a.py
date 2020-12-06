with open('day6.txt') as f:
    data = f.read().split("\n\n")

answers = [line.replace("\n", "") for line in data]
total = 0
for p in answers:
    total += len(set(p))
print(total)
