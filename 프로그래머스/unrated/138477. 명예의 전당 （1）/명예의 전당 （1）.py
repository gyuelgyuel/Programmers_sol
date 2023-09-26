def solution(k, score):
    answer = []
    for i in range(len(score)):
        # i일차까지 score 내림차순 sort
        k_list = sorted(score[:i+1],reverse=True)
        # k일차 전엔 마지막 추가 (가장 작은수)
        if len(k_list)<k:
            answer.append(k_list[-1])
        # k일차부터 k번째 큰 수 추가
        else:            
            answer.append(k_list[k-1])
    return answer