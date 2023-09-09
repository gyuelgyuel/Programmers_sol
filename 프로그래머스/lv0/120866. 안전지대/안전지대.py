def solution(board):
    surround = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for delta in surround:
                    d_i, d_j = delta
                    if (i+d_i>=0 and i+d_i<n) and (j+d_j>=0 and j+d_j<n):
                        if board[i+d_i][j+d_j] == 0:
                            board[i+d_i][j+d_j] = 2
    answer = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                answer += 1
                   
    return n*n - answer