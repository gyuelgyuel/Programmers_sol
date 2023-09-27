def solution(cards1, cards2, goal):
    for g_word in goal:
        not_exist = True
        if len(cards1)!=0:
            if g_word==cards1[0]:
                cards1.remove(g_word)
                not_exist = False
        if len(cards2)!=0:
            if g_word==cards2[0]:
                cards2.remove(g_word)
                not_exist = False
        if not_exist:
            return "No"
    return "Yes"