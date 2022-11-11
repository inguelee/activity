from sys import stdin

N = int(stdin.readline())

NN = N
count = 0
if NN % 5 == 0:
    print(NN // 5)
    exit(0)
else:
    while NN > 0:
        NN -= 3
        count += 1
        if NN % 5 == 0:
            count += NN // 5
            NN = 0

if NN < 0:
    print(-1)
else:
    print(count)