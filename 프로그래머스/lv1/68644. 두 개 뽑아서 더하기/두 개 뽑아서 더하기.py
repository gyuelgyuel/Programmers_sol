def solution(numbers):
    answer = []
    # 첫번째 수
    for i in range(len(numbers)):
        # 두번째 수는 첫번째 수 이후 숫자에서 선택
        for j in range(i+1,len(numbers)):
            sum2 = numbers[i]+numbers[j]
            # sum2가 있으면 append 안함
            if sum2 not in answer:
                answer.append(sum2)
    answer.sort()
    return answer