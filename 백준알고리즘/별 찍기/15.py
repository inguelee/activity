N = int(input())

s = ''

for i in range(1, N + 1):
    s = ' ' * (N - i) + '*' * bool(i - 1) + ' ' * (i * 2 - 3) + '*'
    print(s)
