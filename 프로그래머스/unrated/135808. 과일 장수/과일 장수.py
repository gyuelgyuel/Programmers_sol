def solution(k, m, score):
    answer = 0
    l = len(score)
    score.sort(reverse=True)    # 내림차순 정렬
    for i in range(l//m):       # 최대 사과박스만큼 반복
        answer += min(score[i*m:i*m+m]) * m
    return answer