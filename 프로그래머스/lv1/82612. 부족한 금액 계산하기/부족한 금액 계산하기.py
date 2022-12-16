def solution(price, money, count):
    s = 0
    
    for i in range(1, count + 1):
        s += i * price
    if s < money:
        return 0
    answer = s - money

    return answer