def solution(n):
    w = "수박"
    # w가 두글자이므로 2로 나눈 몫만큼 곱하기, 홀수일때도 마지막에 수박을 잇기 위해 +1
    answer = w * ((n+1)//2)
    return answer[:n]