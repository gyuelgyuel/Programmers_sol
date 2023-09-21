def solution(s):
    # 첫번째 글자는 무조건 -1
    answer = [-1]
    for i in range(1,len(s)):
        # 앞의 문자들을 거꾸로 인덱싱해서 해당 문자를 찾아 인덱스 반환
        x = s[i-1::-1].find(s[i])
        # 인덱스는 0부터 시작하므로 +1
        if x>=0:
            x += 1
        answer.append(x)
    return answer