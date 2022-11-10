import math
import sys
N, K = map(int, sys.stdin.readline().split())

print(int(math.factorial(N) / (math.factorial(K) * math.factorial(N-K))))