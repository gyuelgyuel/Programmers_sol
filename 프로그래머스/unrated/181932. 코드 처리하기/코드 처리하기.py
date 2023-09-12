def solution(code):
    ret = ''
    mode = 0
    for i in range(len(code)):
        if code[i] == "1":
            mode = abs(mode - 1)
        else:
            if mode == 0 and i % 2 == 0:
                ret = ret + code[i]
            elif mode == 1 and i % 2 == 1:
                ret = ret + code[i]
    if len(ret)==0:
        return "EMPTY"
    return ret