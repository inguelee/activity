m = 1

for i in range(3):
    a = int(input())
    m *= a

s = str(m)
b = []

for i in range(10):
    b.append(0)
    b[i] = s.count(str(i))

for i in range(10):
    print(b[i])