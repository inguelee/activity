import sys

N = int(sys.stdin.readline())
arr = [int(x) for x in sys.stdin.readline().split()]

def issosu(num):
    if num == 1:
        return False
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

c = 0
for i, v in enumerate(arr):
    if issosu(v):
        c += 1

print(c)