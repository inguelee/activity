def solution(n):
    n = str(n)
    n = list(n)
    n.reverse()
    answer = list(map(int, n))
    return answer