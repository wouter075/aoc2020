with open('day4.txt') as f:
    # lines = [line.rstrip() for line in f]
    data = f.read()

passports = data.split("\n\n")
passports = list(filter(None, passports))
passports = [line.replace("\n", " ") for line in passports]

checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
valid = 0

for passport in passports:
    parts = passport.split(" ")
    fields = []
    data = []

    for p in parts:
        if p:
            fields.append(p.split(":")[0])
            data.append(p.split(":"))

    count = 0
    for c in checks:
        if c in fields:
            count += 1

    if count == len(checks):
        # check fields:
        v = 0
        for d in data:
            if d[0] == "byr" and 1920 <= int(d[1]) <= 2002:
                v += 1
            if d[0] == "iyr" and 2010 <= int(d[1]) <= 2020:
                v += 1
            if d[0] == "eyr" and 2020 <= int(d[1]) <= 2030:
                v += 1
            if d[0] == "hgt":
                if "cm" in d[1]:
                    if 150 <= int(d[1][:-2]) <= 193:
                        v += 1
                if "in" in d[1]:
                    if 59 <= int(d[1][:-2]) <= 76:
                        v += 1
            if d[0] == "hcl" and d[1][:1] == "#" and len(d[1]) == 7:
                v += 1
            if d[0] == "ecl" and d[1] in ecl:
                v += 1
            if d[0] == "pid" and len(d[1]) == 9 and d[1].isdigit():
                v += 1

        if v == 7:
            valid += 1


print(f"Found {valid} valid passports")
