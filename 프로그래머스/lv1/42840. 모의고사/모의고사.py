def solution(answers):
    # 1~3번 학생 답안 패턴
    sols = [[1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    scores = [0,0,0]    # 점수 기록
    
    for i in range(len(answers)):
        for j in range(3):  # 정답과 답안 비교
            if answers[i]==sols[j][i%len(sols[j])]:
                scores[j]+=1
    
    answer=[]
    for i in range(3):  # 최고 점수 학생번호 기록
        if scores[i]==max(scores):
            answer.append(i+1)
    
    return answer