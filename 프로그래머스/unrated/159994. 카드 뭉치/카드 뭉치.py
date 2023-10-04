def solution(cards1, cards2, goal):
    for g_word in goal:
        not_exist = True            # 원하는 단어 없으면 True
        if len(cards1)!=0:
            if g_word==cards1[0]:   # cards1의 다음카드와 같으면
                cards1.remove(g_word)   # 카드더미에서 카드 제거
                not_exist = False   # 원하는 단어 있음으로 변경
        if len(cards2)!=0:
            if g_word==cards2[0]:
                cards2.remove(g_word)
                not_exist = False
        if not_exist:   # 원하는 단어 없으면 no return
            return "No"
    return "Yes"