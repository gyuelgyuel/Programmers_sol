def solution(n):
    # 3진법수 저장할 string
    tin_digit = ""
    # 3으로 나눈 나머지를 3진법 각 자리수에 저장 (0의 자리수 -> 3^n의 자리수 순으로 저장)
    while n != 0:
        tin_digit = tin_digit + str(n%3)
        n = n//3
    return int(tin_digit,3)