def solution(arr1, arr2):
    answer = arr1.copy()
    n = len(arr1)
    m = len(arr1[0])
    for i in range(n):
        for j in range(m):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer