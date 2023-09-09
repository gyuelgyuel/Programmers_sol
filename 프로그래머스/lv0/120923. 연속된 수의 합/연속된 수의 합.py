def solution(num, total):
    s = num*(num+1)//2
    start = (total-s)//num + 1
    return list(range(start, start+num))