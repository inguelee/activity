N = list(map(int, input().split()))

for i in range(5):
    N[i] **= 2

print(sum(N) % 10)