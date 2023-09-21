def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b + n%a  # 바꿔서 얻은 것 + 못바꿔서 남은 것
    return answer