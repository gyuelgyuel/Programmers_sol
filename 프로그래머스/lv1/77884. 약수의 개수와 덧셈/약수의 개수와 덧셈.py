import math
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if i == int(math.sqrt(i))**2:
            answer -= i
        else:
            answer += i
    
    return answer