def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i != ' ':
            if idx % 2 == 0:
                answer = answer + i.upper()
            else:
                answer = answer + i.lower()
            idx += 1
        else:
            answer = answer + ' '
            idx = 0
    return answer