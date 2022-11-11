from sys import stdin

N = int(stdin.readline())
arr = []
for i in range(N):
    a, b = stdin.readline().split()
    arr.append([int(a), b])

arr.sort(key=lambda arr: arr[0])

for i, j in arr:
    print(i, j)