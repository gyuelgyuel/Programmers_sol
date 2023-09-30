def solution(lottos, win_nums):
    rank = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}   # 맞춘 개수에 따른 순위
    zero_cnt = 0
    ans_cnt = 0
    for num in lottos:
        if num!=0:
            for ans in win_nums:
                if num==ans:
                    ans_cnt += 1
        else:
            zero_cnt += 1
    return [rank[ans_cnt+zero_cnt],rank[ans_cnt]]   # 최대는 zero 다맞춘 경우