N = int(input())

x = 0

for i in range(1, 2 * N):
    if i <= N:
        x += 1
    else:
        x -= 1
    s = '*' * ((N * 2) - (x * 2) + 1)
    print(s.rjust(N * 2 - x))
