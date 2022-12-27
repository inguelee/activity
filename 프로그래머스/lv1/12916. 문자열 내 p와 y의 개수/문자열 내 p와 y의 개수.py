def solution(s):
    s = s.lower()
    answer = True if s.count('p') == s.count('y') else False
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    print(s.count('p'))
    return answer