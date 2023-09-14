def solution(number):
    answer = 0
    # 첫번째 수 고르기
    for i in range(len(number)):
        # 첫번째 수 위치 이후에서 두번째 수 고르기 (이후에서 안고르면 중복 조합 가능성 생김)
        for j in range(i+1,len(number)):
            # 두번째 수 위치 이후에서 세번째 수 고르기
            for k in range(j+1,len(number)):
                # 합이 0이면 answer + 1
                if number[i]+number[j]+number[k] == 0:
                    answer += 1
    return answer