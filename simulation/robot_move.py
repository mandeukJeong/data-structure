def solution(moves):
    x = y = 0
    tmp = 1
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for c in moves:
        if c == 'G':
            x = x + dx[tmp]
            y = y + dy[tmp]
        elif c == 'L':
            tmp = (tmp - 1) % 4
        else:
            tmp = (tmp + 1) % 4

    return [x, y]
                      
print(solution('GGGRGGG'))
print(solution('GGRGGG'))
print(solution('GGGGGGGRGGGRGGRGGGLGGG'))
print(solution('GGLLLGLGGG'))
