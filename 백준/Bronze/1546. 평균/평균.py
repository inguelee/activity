N = int(input())
a = list(map(int, input().split(' ')))

s = (sum(a) / N) / max(a) * 100
print(s)