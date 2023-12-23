N, M = map(int,input().split())
result = [0] * N

for _ in range(M):
    i, j, k = map(int,input().split())
    for a in range(i-1, j):
        result[a] = k
        
for a in result:
    print(a, end=' ')