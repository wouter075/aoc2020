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
        # all_bags[bag_color] = {0: {
        #     'color': bag_contains_color,
        #     'count': bag_contains_number
        # }}
        all_bags[bag_color] = []
        # all_bags[bag_color].extend(bag_contains_color)
        all_bags[bag_color].append(bag_contains_color)

        for x in range(1, len(parts)):
            d = parts[x].split(" ")
            num = int(d[0])
            color = f"{d[1]} {d[2]}".replace(".", "")

            # all_bags[bag_color].update({x: {
            #     'color': color,
            #     'count': num
            # }})
            # print(color)
            all_bags[bag_color].append(color)
        # print(contains)
        # all_bags[bag_color] = contains
    else:
        # single
        # striped olive bags contain 4 dark crimson bags.
        bag_color, bag_contains_number, bag_contains_color = extract_bag(line)
        # all_bags[bag_color] = {0: {
        #     'color': bag_contains_color,
        #     'count': bag_contains_number
        # }}
        all_bags[bag_color] = []
        # all_bags[bag_color].append(bag_contains_color)

print(all_bags)

# http://kmkeen.com/python-trees/
bag_list = []

def children(token, tree):
    "returns a list of every child"
    print("X")
    visited = set()
    to_crawl = deque([token])
    while to_crawl:
        current = to_crawl.popleft()
        if current in visited:
            continue
        visited.add(current)
        node_children = set(tree[current])
        to_crawl.extend(node_children - visited)
    return list(visited)


print(children('shiny gold', all_bags))



# first: 49
