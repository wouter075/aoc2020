with open('day7.txt') as f:
    lines = [line.rstrip() for line in f]


def extract_bag(bag):
    bc = bag.split(" bags contain ")[0]
    bcn = bag.split(" contain ")[1].split(" ")[0]
    bcc = bag.split(f" bags contain {bcn} ")[1].replace(" bags.", "")\
        .replace(" bags", "").replace(" bag.", "").replace(" bag", "")

    if bcn == "no":
        bcn = 0
        bcc = ""
    else:
        bcn = int(bcn)

    return bc, bcn, bcc


all_bags = {}

for line in lines:
    if ", " in line:
        # multiple
        parts = line.split(", ")
        contains = []

        bag_color, bag_contains_number, bag_contains_color = extract_bag(parts[0])
        all_bags[bag_color] = {0: {
            'color': bag_contains_color,
            'count': bag_contains_number
        }}

        for x in range(1, len(parts)):
            d = parts[x].split(" ")
            num = int(d[0])
            color = f"{d[1]} {d[2]}".replace(".", "")

            all_bags[bag_color].update({x: {
                'color': color,
                'count': num
            }})

    else:
        # single
        # striped olive bags contain 4 dark crimson bags.
        bag_color, bag_contains_number, bag_contains_color = extract_bag(line)
        all_bags[bag_color] = {0: {
            'color': bag_contains_color,
            'count': bag_contains_number
        }}

# print(all_bags)
for a in all_bags:
    print(a)
    print(all_bags[a])
    print("")

bag_list = []
count = 0

string = ""


def follow(bags):
    print(bags)
    for b in bags.keys():
        color = bags[b]['color']
        if bags[b]['count'] > 0:
            # string += f"{}"
            bag_list.append(color)
            # count += 1
            follow(all_bags[color])


follow(all_bags['shiny gold'])
print(count)
print("-"*20)
print(len(bag_list))
print(bag_list)
# first: 49
