a = input().split(' ')
a = list(map(int,a))

if sorted(a) == a:
    print("ascending")
elif sorted(a, reverse=True) == a:
    print("descending")
else:
    print("mixed")