import sys
N = int(sys.stdin.readline())

a = []

for i in range(N):
    a.append(list(map(int, sys.stdin.readline().split())))

a.sort()

for i in range(N):
    print(a[i][0], a[i][1])