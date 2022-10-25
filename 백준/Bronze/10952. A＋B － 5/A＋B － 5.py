S = []

while True:
    A, B = map(int, input().split())

    if A == 0 and B == 0:
        break
    else:
        S.append(A + B)

for i in range(len(S)):
    print(S[i])