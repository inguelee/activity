import sys
N, M = map(int, sys.stdin.readline().split())

a = [int(i) for i in sys.stdin.readline().split()]
s = []

for i in range(len(a)-2):
        for j in range(i+1, len(a)-1):
            for k in range(j+1, len(a)):
                if a[i]+a[j]+a[k] <= M:
                    s.append(a[i]+a[j]+a[k])

print(max(s))