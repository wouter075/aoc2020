with open('day12.txt') as f:
    lines = [line.rstrip() for line in f]


compass = {'N': 0, 'E': 0, 'S': 0, 'W': 0, 'R': "E"}

for line in lines:
    cmd = line[:1]
    val = int(line[1:])

    if cmd == "F":
        r = compass["R"]
        compass[r] += val

    if cmd in "NSEW":
        compass[cmd] += val

    if cmd == "R":
        s = list(compass.keys()).index(compass["R"])
        new = list(compass)[int(s + ((val / 90) % 4))]
        compass["R"] = new

    if cmd == "L":
        s = list(compass.keys()).index(compass["R"])
        new = list(compass)[int(s - ((val / 90) % 4))]
        compass["R"] = new



    print(f"cmd: {cmd} - val: {val}")
    print(compass)
    print("")
# print(compass)
