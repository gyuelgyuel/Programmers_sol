def solution(N, stages):
    fail_pct = [[i+1,0,0] for i in range(N+1)]    # 각 요소는 [스테이지 번호, 실패 플레이어 수, 도달 플레이어 수]
    for stage in stages:
        for i in range(stage):  # 스테이지 위치보다 낮은 스테이지 도달 플레이어수 +1
            fail_pct[i][2] += 1
        fail_pct[stage-1][1] += 1 # 스테이지 실패 플레이어 수 + 1
    fail_pct = fail_pct[:N]
    # 실패율 기준 정렬, 같다면 번호 기준 정렬
    fail_pct.sort(key=lambda x: (x[1]/x[2],-1*x[0]) if x[2]!=0 else (0,-1*x[0]), reverse=True)
    # 스테이지 번호 추출
    answer = []
    for i in fail_pct:
        answer.append(i[0])
    return answer