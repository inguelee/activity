from sys import stdin
N = int(stdin.readline())
A = {int(i) for i in stdin.readline().split()}

M = int(stdin.readline())
B = [int(i) for i in stdin.readline().split()]

an = ""
for i, v in enumerate(B):
    an += str(int(v in A)) + '\n'

print(an)