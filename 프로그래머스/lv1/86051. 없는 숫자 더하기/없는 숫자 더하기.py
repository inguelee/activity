def solution(numbers):
    arr = [i for i in range(10)]
    answer = sum(arr) - sum(numbers)
    return answer