from sys import stdin
a = []
s = []
for i in range(int(stdin.readline())):
    a.append(stdin.readline().split())

for i, v in enumerate(a):
    if v[0] == "push":
        s.append(int(v[-1]))
    elif v[0] == "pop":
        if len(s):
            print(s.pop(0))
        else:
            print(-1)
    elif v[0] == "size":
        print(len(s))
    elif v[0] == "empty":
        if len(s):
            print(0)
        else:
            print(1)
    elif v[0] == "front":
        if len(s):
            print(s[0])
        else:
            print(-1)
    elif v[0] == "back":
        if len(s):
            print(s[-1])
        else:
            print(-1)