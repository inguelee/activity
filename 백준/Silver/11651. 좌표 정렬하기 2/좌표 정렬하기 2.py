import sys
N = int(sys.stdin.readline())

a = []

for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    a.append([y, x])

a.sort()

for i in range(N):
    print(a[i][1], a[i][0])