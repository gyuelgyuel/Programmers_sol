def solution(n):
    num3x = 0
    for i in range(n):
        num3x += 1
        while (num3x%3==0)or(str(num3x).find("3")!=-1): 
            if num3x % 3 == 0:
                num3x += 1
            elif str(num3x).find("3")!=-1:
                num3x += 1
    return num3x