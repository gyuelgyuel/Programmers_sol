def solution(l, r):
    answer = []
    for i in range((l//5)*5,(r//5+1)*5):
        string = str(i)
        is5n0 = True
        for s in string:
            if s!="0" and s!="5":
                is5n0 = False
        if is5n0:
            answer.append(i)
    if len(answer)==0:
        return [-1]
    return answer