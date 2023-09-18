def solution(s):
    num_dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = 0
    word = ''
    for w in s:
        try:    # w가 int로 변환 가능하면 변환하고 answer에 저장
            answer = answer*10 + int(w)
        except: # w가 int로 변환 불가능하면 word에 저장
            word += w
            try:    # word가 dictionary에 있으면 answer에 저장
                answer = answer*10 + num_dic[word]
                word = ''
            except:
                pass
    return answer