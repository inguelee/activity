def solution(n):
    s = sorted(str(n), reverse=True)
    answer = int(''.join(s))
    return answer