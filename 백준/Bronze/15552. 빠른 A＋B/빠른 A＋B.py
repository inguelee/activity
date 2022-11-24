from sys import stdin
T = int(stdin.readline())
arr = [0 for _ in range(T)]

for i in range(T):
    A, B = map(int, stdin.readline().split())
    arr[i] = A + B

an = ""
for i in arr:
    an += str(i) + '\n'

print(an.rstrip())