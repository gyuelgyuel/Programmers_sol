def solution(n):
    answer = [[0]*n for i in range(n)]
    row = 0
    col = 0
    start_len = 0
    end_len = n-1
    dir_dic = {"r": (0,1), "d": (1,0), "l": (0,-1), "u": (-1,0)}
    direction = "r"
    for i in range(1,n**2+1):
        answer[row][col]=i
        d_row, d_col = dir_dic[direction]
        row += d_row
        col += d_col
        if row == start_len and col == start_len:
            direction = "r"
            start_len += 1
            end_len -= 1
            row += 1
            col += 1
        elif row == start_len and col == end_len:
            direction = "d"
        elif row == end_len and col == end_len:
            direction = "l"
        elif row == end_len and col == start_len:
            direction = "u"
            
            
    return answer