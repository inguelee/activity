import math

def solution(n, m):
    nn = n
    mm = m
    i = 2
    j = 2
    while nn != mm:
        if nn < mm:
            nn = n * i
            i += 1
        else:
            mm = m * j
            j += 1
    answer = [math.gcd(n,m), mm]
    return answer