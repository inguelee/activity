from sys import stdin
a = []
s = []

for _ in range(int(stdin.readline())):
    a.append(stdin.readline().split())

for i, v in enumerate(a):
    if v[0] == "push_front":
        s.insert(0, int(v[-1]))
    elif v[0] == "push_back":
        s.append(int(v[-1]))
    elif v[0] == "pop_front":
        if len(s):
            print(s.pop(0))
        else:
            print(-1)
    elif v[0] == "pop_back":
        if len(s):
            print(s.pop())
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