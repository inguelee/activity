import sys

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr.sort()

for i, v in enumerate(arr):
    print(v)