N = int(input())

for i in range(1, N+1):
    s = '*' * (2 * i - 1)
    print(s.rjust(N+i-1))
