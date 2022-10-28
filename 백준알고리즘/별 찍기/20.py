N = int(input())

sw = True

for i in range(1, N + 1):
    if sw == True:
        s = '* ' * N
        s = s[:-1]
        print(s)
        sw = False
    else:
        s = ' *' * N
        print(s)
        sw = True
