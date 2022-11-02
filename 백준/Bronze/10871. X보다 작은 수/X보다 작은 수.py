N, X = map(int, input().split())
A = list(map(int, input().split()))
AA = A[:]

for i in A:
    if i >= X:
        AA.remove(i)

for i in range(len(AA)):
    print(AA[i], end=' ')