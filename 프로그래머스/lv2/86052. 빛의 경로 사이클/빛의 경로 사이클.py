def solution(grid):
    answer = []
    rows = len(grid)
    cols = len(grid[0])
    visited = [[[False for _ in range(4)] for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(4):
                now = [i,j,k]
                length = 0
                while not visited[now[0]][now[1]][now[2]]:
                    visited[now[0]][now[1]][now[2]]=True
                    d_num = now[2]
                    x = (now[0] + int((d_num%2)*(0.5-d_num//2)*2))%rows
                    y = (now[1] + int(((d_num+1)%2)*(0.5-d_num//2)*2))%cols
                    if grid[x][y]=='S':
                        d = now[2]
                    elif grid[x][y]=='R':
                        d = (d_num+1)%4
                    elif grid[x][y]=='L':
                        d = (d_num-1)%4
                    else:
                        print('error')
                        break
                    now = [x,y,d]
                    length+=1
                if length != 0:
                    answer.append(length)
    return sorted(answer)
