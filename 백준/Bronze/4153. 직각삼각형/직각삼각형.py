from sys import stdin

while True:
    a = [int(i) for i in stdin.readline().split()]
    a.sort()
    if a[2] == 0 and a[1] == 0 and a[0] == 0:
        break
    if a[2] ** 2 == (a[1] ** 2) + (a[0] ** 2):
        print("right")
    else:
        print("wrong")