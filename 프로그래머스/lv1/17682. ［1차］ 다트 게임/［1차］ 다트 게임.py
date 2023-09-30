def solution(dartResult):
    answer = 0
    num = [0,0]     # 숫자 임시 저장 배열 *옵션때문에 길이 2
    bonus = ['S','D','T']
    num_start = True
    for s in dartResult:
        s_ascii = ord(s)
        if s_ascii>47 and s_ascii<58: # 숫자인 경우, 이전 숫자 누적 후 새로운 숫자 저장
            if num_start:
                print(num[0], end=' ')
                answer += num[0]
                num[0] = num[1]     # 이전 숫자
                num[1] = s_ascii-48 # 새 숫자
                num_start=False     # 다음에도 숫자가 올시 첫 숫자가 아님을 알림
            else:
                num[1] = num[1]*10+s_ascii-48   # 앞의 자리 올리고, 일의자리 더하기
        elif s in bonus:
            num[1] = num[1]**(bonus.index(s)+1)   # 해당하는 bonus 제곱
            num_start = True    # 새로운 숫자 받을 준비
        else:   # 옵션
            if s=='*':
                num[0]=num[0]*2
                num[1]=num[1]*2
            else:
                num[1]=num[1]*(-1)
    print(num[0],num[1], end=' ')
    answer += num[0]+num[1]    # 누적 안된 숫자 누적

    return answer