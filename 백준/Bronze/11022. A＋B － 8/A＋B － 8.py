T = int(input())
S = []
for _ in range(T):
    A, B = map(int, input().split())
    S.append([A,B,A+B])

for i, v in enumerate(S):
    print("Case #{0}: {1} + {2} = {3}".format(i+1, v[0], v[1], v[2]))