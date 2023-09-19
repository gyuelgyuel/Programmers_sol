def solution(array, commands):
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])    # i-1 부터 j-1까지 sort한 배열의 k-1 번째를 append
    return answer