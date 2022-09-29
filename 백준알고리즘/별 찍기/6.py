N = int(input())

for i in range(N, 0, -1):
    s = '*' * (i * 2 - 1)
    print(s.rjust((N - 1) + i))
