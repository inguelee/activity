N = int(input())

for i in range(1, N):
    s = ' ' * (N - i) + '*' * bool(i - 1) + ' ' * ((i * 2) - 3) + '*'
    print(s)

print('*' * (N * 2 - 1))
