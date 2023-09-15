def solution(s):
    q = []  # queue style
    for l in s:
        if l == "(":
            q.append(l)
        else:
            if len(q)==0:
                return False
            else:
                q.pop()
    if len(q) != 0:
        return False
    else:
        return True