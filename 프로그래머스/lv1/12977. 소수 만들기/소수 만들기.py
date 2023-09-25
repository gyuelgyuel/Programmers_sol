def is_prime(num):  # 소수 판별 함수
    max_div = int(num**0.5)
    div = 2
    while div <= max_div:   # div 1씩 증가시키며, 루트값까지만 while문 돌리기
        if num%div==0:      # 소수가 아니면 return False
            return False
        else:
            div += 1
    return True

def solution(nums):
    answer = 0
    l = len(nums)
    for i in range(l-2):    # 서로 다른 3개 수 뽑기
        for j in range(i+1,l-1):
            for k in range(j+1,l):
                num = nums[i]+nums[j]+nums[k]
                if is_prime(num):   # 더한값이 소수면 ans +1
                    answer += 1
    return answer