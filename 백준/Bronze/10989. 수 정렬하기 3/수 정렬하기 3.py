import sys

N = int(sys.stdin.readline())

arr = [0] * 10000
for i in range(N):
    n = int(sys.stdin.readline())
    arr[n-1] += 1

for i in range(10000):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i+1)