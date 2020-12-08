with open('day8.txt') as f:
    lines = [line.rstrip() for line in f]

instructions = []

for line in lines:
    ins, parm = line.split(" ")
    parm = int(parm)
    # print(f"ins: {ins}, parm: {parm}")
    instructions.append([ins, parm])

acc = 0
walked = []


def walk(next):
    global acc

    inst = instructions[next]
    # print(inst)
    if next in walked:
        print("Hey, we hebben dit al een keer gedaan!")
        return
    else:
        walked.append(next)

    if inst[0] == "nop":
        next += 1
    if inst[0] == "acc":
        acc += inst[1]
        next += 1
    if inst[0] == "jmp":
        next += inst[1]
    print(f"instruction: {inst[0]} acc: {acc} | next: {next}")
    walk(next)


# walk(0)
# print(acc)



