with open('day4.txt') as f:
    # lines = [line.rstrip() for line in f]
    data = f.read()

passports = data.split("\n\n")
passports = list(filter(None, passports))
passports = [line.replace("\n", " ") for line in passports]

checks = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid = 0

for passport in passports:
    parts = passport.split(" ")
    fields = []
    data = []

    for p in parts:
        fields.append(p.split(":")[0])

    count = 0
    for c in checks:
        if c in fields:
            count += 1

    if count == len(checks):
        print(" ".join(fields))
        valid += 1

print(f"Found {valid} valid passports")
