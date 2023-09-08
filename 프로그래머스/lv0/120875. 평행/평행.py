def solution(dots):
    d1 = dots[0]
    copy = dots[1:]
    for d2 in copy:
        copy.remove(d2)
        grad1 = (d1[1]-d2[1]) / (d1[0]-d2[0])   # 직선1 기울기
        d3, d4 = copy
        grad2 = (d3[1]-d4[1]) / (d3[0]-d4[0])   # 직선2 기울기
        if grad1 == grad2:
            return 1
        else:
            copy = dots[1:]
    return 0