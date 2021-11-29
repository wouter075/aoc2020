p1 = [14, 29, 25, 17, 13, 50, 33, 32, 7, 37, 26, 34, 46, 24, 3, 28, 18, 20, 11, 1, 21, 8, 44, 10, 22]
p2 = [5, 38, 27, 15, 45, 40, 43, 30, 35, 9, 48, 12, 16, 47, 42, 4, 2, 31, 41, 39, 23, 19, 36, 49, 6]
rnd = 1

while True:
    sp1 = [str(i) for i in p1]
    sp2 = [str(i) for i in p2]

    print(f"-- Round {rnd} --")
    print(f"Player 1's deck: {', '.join(sp1)}")
    print(f"Player 2's deck: {', '.join(sp2)}")
    print(f"Player 1 plays: {p1[0]}")
    print(f"Player 2 plays: {p2[0]}")
    if p1[0] > p2[0]:
        print(f"Player 1 wins the round!")
        p1.append(p1[0])
        p1.append(p2[0])
    else:
        print(f"Player 2 wins the round!")
        p2.append(p2[0])
        p2.append(p1[0])
    del p1[0]
    del p2[0]
    rnd += 1

    if len(p1) == 0 or len(p2) == 0:
        break

score = 0
c = 1
if len(p2) == 0:
    # player 1 wins:
    p1.reverse()
    for p in p1:
        score += p * c
        c += 1
    print(f'Player 1 wins! The score is: {score}')
else:
    # player 2 wins:
    p2.reverse()
    for p in p2:
        score += p * c
        c += 1
    print(f'Player 2 wins! The score is: {score}')
