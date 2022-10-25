nn = int(input())

S = []

for _ in range(nn):
    n = 0
    s = 0
    ss = input()
    for i in ss:
        if i == 'O':
            n += 1
            s += n
        else:
            n = 0
    S.append(s)

for i in range(nn):
    print(S[i])