def solution(s):
    num = sorted(list(map(int, s.split(' '))))
    return str(num[0]) + ' ' + str(num[-1])