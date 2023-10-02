def solution(X, Y):
    answer = ''
    x_num = [0]*10
    y_num = [0]*10
    # x 숫자 개수 기록
    for i in X:
        x_num[int(i)] += 1
    # y 숫자 개수 기록
    for i in Y:
        y_num[int(i)] += 1

    # x,y 숫자 개수 중 적은 개수 기록 (둘다 가지고 있는 개수)
    couple = list(map(min, zip(x_num,y_num)))
    # 9~0까지 answer에 개수만큼 append
    for i in range(9,-1,-1):
        answer += str(i)*couple[i]
    if answer == '':        # 공통 수가 없는 경우
        return '-1'
    if answer[0] == '0':    # 공통 수가 0뿐인 경우
        return '0'
    return answer