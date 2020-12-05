with open('day5.txt') as f:
    boarding_passes = [line.rstrip() for line in f]


def find_missing(lst):
    return [x for x in range(lst[0], lst[-1]+1) if x not in lst]


seat_list = []
for boarding_pass in boarding_passes:
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[-3:].replace("L", "0").replace("R", "1"), 2)
    seat = row * 8 + col
    seat_list.append(seat)

print(find_missing(sorted(seat_list)))
