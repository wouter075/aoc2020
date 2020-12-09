with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

instructions = []
for line in lines:
    ins, parm = line.split(" ")
    parm = int(parm)
    instructions.append([ins, parm])


def walk(n, i):
    global acc

    inst = i[n]
    if inst[0] == "nop":
        n += 1
    if inst[0] == "acc":
        acc += inst[1]
        n += 1
    if inst[0] == "jmp":
        n += inst[1]

    walk(n, i)


def inst_count(inst):
    c = 0
    for i in instructions:
        if i[0] == inst:
            c += 1
    return c


def inst_change(old_inst, new_inst, pos):
    c = 0
    ic = instructions
    ni = []
    for k, v in ic:
        if k == old_inst:
            if c == pos:
                k = new_inst
            c += 1
        ni.append([k, v])
    return ni


nop = inst_count("nop")
jmp = inst_count("jmp")


for nn in range(0, nop):
    walked = []
    acc = 0
    nnop = inst_change("nop", "jmp", nn)
    try:
        walk(0, nnop)
    except RecursionError:
        continue

    except IndexError:
        print(acc)

for nj in range(0, jmp):
    walked = []
    acc = 0
    njmp = inst_change("jmp", "nop", nj)
    # print(njmp)
    try:
        walk(0, njmp)
    except RecursionError:
        continue

    except IndexError:
        print(acc)

# 2, 6982, to high