N = int(input())
d = {}

for i in range(N):
    a = input()
    d[a] = len(a)

d = sorted(d.items(), key=lambda x: (x[1], x[0]))

for i in range(len(d)):
    print(d[i][0])