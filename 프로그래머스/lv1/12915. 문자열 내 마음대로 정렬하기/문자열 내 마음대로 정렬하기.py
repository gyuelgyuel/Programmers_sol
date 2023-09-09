def solution(strings, n):
    l = len(strings)
    ## buble sort
    for i in range(l):
        for j in range(l-i-1):
            ## n번째 문자 비교
            if strings[j][n] > strings[j+1][n]:
                temp = strings[j+1]
                strings[j+1] = strings[j]
                strings[j] = temp
            ## 사전순 비교
            elif strings[j][n] == strings[j+1][n]:
                if strings[j] > strings[j+1]:
                    temp = strings[j+1]
                    strings[j+1] = strings[j]
                    strings[j] = temp
    return strings