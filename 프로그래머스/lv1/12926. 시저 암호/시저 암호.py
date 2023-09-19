def solution(s, n):
    answer = ''
    for c in s:
        # 공백일 경우 그대로 입력
        if c == ' ':
            answer += ' '
        else:
            # 대문자
            if ord(c) <= 90:
            # ascii code 상 n을 더한것이 alphabet 범위가 아닐 경우를 대비하여 알파벳 총 갯수 26으로 나눈 나머지를 입력
                answer += chr((ord(c) + n-65)%26+65)
            # 소문자
            else:
                answer += chr((ord(c) + n-97)%26+97)
                
    return answer