def solution(sizes):
    # w를 긴변, h를 짧은변으로 놓고 해결
    # 긴변 기준 정렬
    sizes.sort(key = lambda x: max(x))
    # 긴변 중 가장 큰것
    w_max = max(sizes[-1])
    # 짧은변 기준 정렬
    sizes.sort(key = lambda x: min(x))
    # 짧은변 중 가장 큰것
    h_max = min(sizes[-1])
    return w_max*h_max