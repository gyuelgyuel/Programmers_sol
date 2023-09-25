def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        div_max = int(i**0.5)
        div = 1
        i_pow = 0
        while div<=div_max:
            if i%div==0:
                i_pow += 2
            div += 1
        if i == int(i**0.5)**2:
            i_pow -= 1
        if i_pow > limit:
            answer += power
        else:
            answer += i_pow
    return answer