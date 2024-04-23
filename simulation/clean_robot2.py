def solution(n, moves): 
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    dir = ['U', 'R', 'D', 'L']

    for c in moves:
        for k in range(4):
            if c == dir[k]:
                nx = x + dx[k]
                ny = y + dy[k]

                if nx >= 0 and nx < n and ny >= 0 and ny < n:
                    x = nx
                    y = ny

    return [x, y]    
                
print(solution(5, 'RRRDDDUUUUUUL'))
print(solution(7, 'DDDRRRDDLL'))
print(solution(5, 'RRRRRDDDDDU'))
print(solution(6, 'RRRRDDDRRDDLLUU'))

