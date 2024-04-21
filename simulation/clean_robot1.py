def solution(moves):
    x = y = 0
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for sH in moves:
        if sH == 'U':
            nx = x + dx[0]
            ny = y + dy[0]
        elif sH == 'R':
            nx = x + dx[1]
            ny = y + dy[1]
        elif sH == 'L':
            nx = x + dx[3]
            ny = y + dy[3]
        else:
            nx = x + dx[2]
            ny = y + dy[2]

        if nx >= 0 and nx < 100 and ny >= 0 and ny < 100:
            x = nx
            y = ny
    
    return [x, y]
                            
print(solution('RRRDDDLU'))
print(solution('DDDRRRDDLL'))
print(solution('RRRRRRDDDDDDUULLL'))
print(solution('RRRRDDDRRDDLLUU'))
