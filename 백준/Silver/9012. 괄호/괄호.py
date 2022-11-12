from sys import stdin
a = []

for _ in range(int(stdin.readline())):
    aa = stdin.readline()
    a.append(aa[:-1])

an = ""
for i, v in enumerate(a):
    if v.count('(') - v.count(')'):
        an += "NO" + '\n'
    else:
        l = 0
        r = 0
        for j, w in enumerate(v):
            sw = True
            if w == '(':
                l += 1
            else:
                l -= 1
            
            if l < 0:
                an += "NO" + '\n'
                sw = False
                break
        if sw == True:
            an += "YES" + '\n'

print(an[:-1])