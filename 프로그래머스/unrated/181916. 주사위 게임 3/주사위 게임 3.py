def solution(a, b, c, d):
    dices = [a,b,c,d]
    is_same = [[0]*4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if dices[i]==dices[j]:
                is_same[i][j] = 1
    
    num_same = []
    for i in range(4):
        num_same.append(sum(is_same[i]))
    
    if 4 in num_same:
        return 1111 * dices[num_same.index(4)]
    elif 3 in num_same:
        return (10 * dices[num_same.index(3)] + dices[num_same.index(1)])**2
    elif 2 in num_same:
        p = dices[num_same.index(2)]
        copy = dices[:]
        copy.remove(p)
        copy.remove(p)
        q, r = copy
        if q==r:
            return abs(p**2 - q**2)
        else:
            return q*r
    else:
        return min(dices)