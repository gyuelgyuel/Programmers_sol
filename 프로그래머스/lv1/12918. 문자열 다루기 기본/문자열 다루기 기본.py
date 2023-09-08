def solution(s):
    l = len(s)
    if not (l == 4 or l == 6):
        return False
    
    try:
        int(s)
        return True
    except:
        return False