def solution(food):
    answer = ''
    # answer의 중간지점 index 번호
    mid_idx = 0
    for i in range(1,len(food)):
        # 한쪽에 채워야할 i번 음식 개수
        num_food = food[i]//2
        # answer의 중간 지점에 "i"를 i 음식 개수의 2배를 넣는다. (양쪽 집어넣어야하니깐)
        answer = answer[:mid_idx] + str(i) * num_food * 2 + answer[mid_idx:]
        # 중간지점 index 갱신
        mid_idx += num_food
    # 마지막으로 물 넣기
    answer = answer[:mid_idx] + "0" + answer[mid_idx:]
    
    return answer