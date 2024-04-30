def solution(board):
    answer = 0
    x = y = 0
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    tmp1 = []
    tmp2 = []

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                tmp1.append([i, j])

    for i in tmp1:
        for j in range(8):
            nx = i[0] + dx[j]
            ny = i[1] + dy[j]

            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board) and board[nx][ny] != 1:
                tmp2.append((nx, ny))     

    answer = len(set(tmp2))

    return answer
                       
print(solution([[0, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))
print(solution([[1, 0, 0, 1, 0], [0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [0, 1, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1, 0], [0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 1], [0, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0, 0]]))
