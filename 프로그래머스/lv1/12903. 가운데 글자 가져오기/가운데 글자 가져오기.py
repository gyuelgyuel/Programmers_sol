def solution(s):
    i = (len(s)-1)//2
    d = (len(s)-1)%2
    return s[i:i+d+1]