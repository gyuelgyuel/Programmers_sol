def solution(n, lost, reserve):
    reserve.sort()
    i = 0
    while i<len(reserve):           # 여분 챙겨온 사람중 자신이 도난당한 경우 제거
        r = reserve[i]
        if r in lost:
            lost.remove(r)
            reserve.remove(r)
        else:                   # remove 하면 index가 자동으로 당겨짐으로 remove안했을 때만 i +1
            i += 1
            
    for r in reserve:
        if r-1 in lost:         # 앞사람 도난시 빌려주기
            lost.remove(r-1)
        elif r+1 in lost:       # 뒷사람 도난시 빌려주기  (앞사람 도난 아닐때만)
            lost.remove(r+1)
    return n-len(lost)          # 전체 - 못빌린사람