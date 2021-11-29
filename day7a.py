from collections import deque

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
        # all_bags[bag_color] = []
        # all_bags[bag_color].extend(bag_contains_color)
        # all_bags[bag_color].append(bag_contains_color)

        for x in range(1, len(parts)):
            d = parts[x].split(" ")
            num = int(d[0])
            color = f"{d[1]} {d[2]}".replace(".", "")

            all_bags[bag_color].update({x: {
                'color': color,
                'count': num
            }})
            # print(color)
            # all_bags[bag_color].append(color)
        # print(contains)
        # all_bags[bag_color] = contains
    else:
        # single
        # striped olive bags contain 4 dark crimson bags.
        bag_color, bag_contains_number, bag_contains_color = extract_bag(line)
        all_bags[bag_color] = {0: {
            'color': bag_contains_color,
            'count': bag_contains_number
        }}
        # all_bags[bag_color] = []

print(all_bags)
# print("="*100)
checked = []


def check_bag(color):
    for k in all_bags[color].keys():
        if all_bags[color][k]['color']:
            if all_bags[color][k]['color'] == 'shiny gold':
                if all_bags[color][k]['color'] not in checked:
                    checked.append(all_bags[color][k]['color'])
                break
            # else:
            check_bag(all_bags[color][k]['color'])


# for bag in all_bags.keys():
#     # print(bag)
#     check_bag(bag)
#
# print(len(checked))

# first: 49
