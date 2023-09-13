def solution(d, budget):
    cnt = 0
    d.sort()
    for i in d:
        if budget - i < 0:
            break
        budget -= i
        cnt += 1
    
    return cnt