def solution(nums):
    species = len(set(nums))    # set로 변환
    return min(species,len(nums)//2)    # 종류 개수와 총개수의 절반 중 작은 거 반환