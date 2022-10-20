T = int(input())
r = []
s = []

for _ in range(T):
    R, S = input().split()
    R = int(R)
    r.append(R)
    s.append(S)

for i in range(T):
    for j in s[i]:
        print(j * r[i], end='')
    print()