def solution(n, m, section):
    answer = 0
    last_paint = 0  # 앞에서 부터 칠했을 때, 가장 마지막에 칠해진 구역번호
    for s in section:   # 구역을 살피며 칠해진 마지막 구역번호보다 번호가 낮으면 패스
        if s > last_paint:  # 높으면 칠하고, 구역번호 갱신
            last_paint = s+m-1
            answer += 1
    return answer