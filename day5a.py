with open('day5.txt') as f:
    boarding_passes = [line.rstrip() for line in f]

max_seat = 0
for boarding_pass in boarding_passes:
    row = int(boarding_pass[:7].replace("F", "0").replace("B", "1"), 2)
    col = int(boarding_pass[-3:].replace("L", "0").replace("R", "1"), 2)
    seat = row * 8 + col
    if seat > max_seat:
        max_seat = seat
print(max_seat)
