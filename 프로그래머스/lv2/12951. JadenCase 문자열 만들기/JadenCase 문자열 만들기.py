def solution(s):
    answer = ''
    is_first = True
    for l in s:
        if l == ' ':
            answer = answer + l
            is_first = True
        else:
            if is_first:
                answer = answer + l.upper()
                is_first = False
            else:
                answer = answer + l.lower()
                
    return answer