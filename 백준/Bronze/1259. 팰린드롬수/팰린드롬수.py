N = input()
a = []
while N != '0':
    b = 'yes'
    for i in range(len(N) // 2):
        if N[i] != N[len(N)-i-1]:
            b = 'no'
            break
        
    a.append(b)
    N = input()

for i, v in enumerate(a):
    print(v)