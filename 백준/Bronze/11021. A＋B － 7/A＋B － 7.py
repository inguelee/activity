T = int(input())
S = []
for _ in range(T):
    A, B = map(int, input().split())
    S.append(A+B)

for i, v in enumerate(S):
    print("Case #{0}: {1}".format(i+1, v))