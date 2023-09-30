def solution(a, b):
    days = [31,29,31,30,31,30,31,31,30,31,30,31]
    date = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    total_day = sum(days[:a-1]) + b     # a달 전까지 날짜합 + 날짜
    return date[(total_day+3)%7]    # 1월1일이 금요일이므로 +3