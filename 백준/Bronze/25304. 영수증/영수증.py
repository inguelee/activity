import sys

X = int(input())
N = int(input())

for i in range(N):
    a, b = [int(x) for x in sys.stdin.readline().split()]
    X = X - a * b

if X == 0:
    print("Yes")
else:
    print("No")