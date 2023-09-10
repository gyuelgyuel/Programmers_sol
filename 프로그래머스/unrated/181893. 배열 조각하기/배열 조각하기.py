def solution(arr, query):
    count = 0
    for i in query:
        if count % 2 == 0:
            arr = arr[:i+1]
        else:
            arr = arr[i:]
        count += 1
        
    return arr