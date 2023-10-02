def solution(babbling):
    answer = 0  # 발음 가능 단어 카운트
    for w in babbling:
        able = True     # 발음 가능한 단어인지
        last_bab = ''
        while len(w):   # 발음 가능 부분 다 제거하면 while문 종료
            find = False    # 발음 가능 부분을 찾았는지 여부
            if len(w)>=2:
                if w[:2] in ['ye','ma']:        # 앞의 2글자가 2글자 babble과 같으면
                    if last_bab != w[:2]:       # 전의 babble이랑 연속되지 않으면
                        last_bab = w[:2]        # 전의 babble 갱신
                        w = w[2:]               # 앞의 2글자 날리기
                        find = True             # 발음 가능 부분 찾음 표시
                elif len(w)>=3:
                    if w[:3] in ['aya','woo']:  # 앞의 3개가 3글자 babble과 같으면
                        if last_bab != w[:3]:   # 전의 babble이랑 연속되지 않으면
                            last_bab = w[:3]    # 전의 babble 갱신
                            w = w[3:]           # 앞의 3글자 날리기
                            find = True         # 발음 가능 부분 찾음 표시
            else:               # 남은 단어 길이가 2미만일 경우
                able = False    # 불가능 표시
                break
            if not find:        # 못 찾은 경우
                able = False    # 불가능 표시
                break
        if able:            # 가능하면
            answer += 1     # 정답 +1
    return answer