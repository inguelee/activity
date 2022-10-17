N = int(input())

for i in range(1, N + 1):
    s = '* ' * i
    s = s[:-1]
    print(s.rjust(N + i - 1))
