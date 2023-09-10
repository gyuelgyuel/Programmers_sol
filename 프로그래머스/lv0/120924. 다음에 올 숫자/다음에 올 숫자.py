def solution(common):
    e1 = common[0]
    e2 = common[1]
    e3 = common[2]
    
    if e1-e2==e2-e3:
        return common[-1] + e2 - e1
    elif e2//e1==e3//e2:
        return common[-1] * (e2//e1)
    else:
        print("input error")
        return 0