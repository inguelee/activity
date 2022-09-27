N = int(input())

for i in range(N, 0, -1):
    s = '*' * i
    print(s.rjust(N))
