def solution(t, p):
    d = len(p)
    answer = 0
    # 마지막 p의 길이 - 1 만큼 까지 반복문 (index error 방지)
    for i in range(len(t)-d+1):
        # p보다 작으면 answer + 1
        if t[i:i+d] <= p:
            answer += 1
    return answer