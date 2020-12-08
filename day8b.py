with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

instructions = []


def make_inst():
    instructions = []
    for line in lines:
        ins, parm = line.split(" ")
        parm = int(parm)
        instructions.append([ins, parm])
    return instructions


instructions = make_inst()
acc = 0
walked = []


def walk(next):
    global acc

    inst = instructions[next]
    if next in walked:
        return "maxed"
    else:
        walked.append(next)

    if inst[0] == "nop":
        next += 1
    if inst[0] == "acc":
        acc += inst[1]
        next += 1
    if inst[0] == "jmp":
        next += inst[1]
    walk(next)


def inst_count(inst):
    c = 0
    for i in instructions:
        if i[0] == inst:
            c += 1
    return c


def inst_change(inst, new_inst, pos):
    c = 0
    for i in instructions:
        if i[0] == inst:
            if c == pos:
                i[0] = new_inst
            c += 1
    return instructions


#
# walk(0)
# print(acc)
#
# jpm, nop
nop = inst_count("nop")
jmp = inst_count("jmp")

print(f"{nop}, {jmp}")
# print(instructions)
for n in range(0, nop):
    # print(f"nop -> jmp: {n}")
    instructions = inst_change("nop", "jmp", n)
    # print(instructions)
    if walk(0) is not "maxed":
        print(acc)
    instructions = make_inst()

# print(instructions)
# print("-"*20)
for n in range(0, jmp):
    # print(f"jmp -> nop: {n}")
    instructions = inst_change("jmp", "nop", n)
    # print(instructions)
    if walk(0) is not "maxed":
        print(acc)

    instructions = make_inst()

# 1262, to low