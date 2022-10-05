N = int(input())

for i in range(1, N + 1):
    s = '*' * ((i * 2) - 1)
    print(s.rjust(N + i - 1))

for i in range(N - 1, 0, -1):
    s = '*' * ((i * 2) - 1)
    print(s.rjust(N + i - 1))
