def solution(name, yearning, photo):
    answer = []
    for ppls in photo:
        score = 0                       # 사진마다 점수 초기화
        for ppl in ppls:
            try:                        # 찾은 경우만 score 추가
                idx = name.index(ppl)   # 이름 찾아서 index 반환
                score += yearning[idx]
            except:
                pass
        answer.append(score)
    return answer