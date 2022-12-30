def solution(n):
    answer = ''
    sw = True
    for i in range(n):
        if sw:
            answer += '수'
            sw = False
        else:
            answer += '박'
            sw = True
    return answer