a, b = map(list, input().split())

a.reverse()
b.reverse()

a = ''.join(a)
b = ''.join(b)

print(max(a,b))