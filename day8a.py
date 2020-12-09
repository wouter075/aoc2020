with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

instructions = []

for line in lines:
    ins, parm = line.split(" ")
    parm = int(parm)
    instructions.append([ins, parm])

acc = 0
walked = []


def walk(n, i):
    global acc

    inst = i[n]
    # print(inst)
    if n in walked:
        return "maxed"
    else:
        walked.append(n)

    if inst[0] == "nop":
        n += 1
    if inst[0] == "acc":
        acc += inst[1]
        n += 1
    if inst[0] == "jmp":
        n += inst[1]
    walk(n, i)


# walk(0, instructions)
# print(acc)



