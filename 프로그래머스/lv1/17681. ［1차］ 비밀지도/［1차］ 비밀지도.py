def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        string = bin(arr1[i] | arr2[i])[2:]
        string = "0" * (n-len(string)) + string
        answer.append(string.replace("1","#").replace("0"," "))
        
    return answer