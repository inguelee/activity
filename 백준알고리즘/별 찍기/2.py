n = int(input())

for i in range(1, n + 1):
    s = ''
    for j in range(i):
        s += '*'
    print(s.rjust(n))
