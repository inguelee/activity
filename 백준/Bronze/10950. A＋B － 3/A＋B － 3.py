N = int(input())
a = []

for i in range(N):
    x, y = map(int, input().split())
    a.append(x+y)
    
for i in range(N):
    print(a[i])