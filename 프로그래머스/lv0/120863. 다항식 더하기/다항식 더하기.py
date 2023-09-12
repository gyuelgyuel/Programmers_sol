def solution(polynomial):
    before = '0'
    num_list = [0,0]    # [x,상수]
    for s in polynomial:
        if s.isdigit():
            before = before + s
        if s == "x":
            if before == '0':
                before = '1'
            num_list[0] += int(before)
            before = '0'
        elif s == " ":
            num_list[1] += int(before)
            before = '0'
    num_list[1] += int(before)
    answer = ''
    if num_list[0] != 0:
        if num_list[0] == 1:
            answer = "x + "
        else:
            answer = str(num_list[0]) + "x + "
    else:
        answer = ''
    if num_list[1] != 0:
        answer = answer + str(num_list[1])
    else:
        answer = answer[:-3]
    
    return answer