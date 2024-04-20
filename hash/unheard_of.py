from collections import defaultdict
def solution(n, m, name):
    answer = []
    nH = defaultdict(int)
    cnt = 0

    for i in range(n + m):
        if i >= n and name[i] in nH:
            cnt += 1
            answer.append(name[i])
        nH[name[i]] += 1

    sorted(answer)
    print(cnt)
    for i in range(len(answer)):
        print(answer[i])
    
arr = []
n, m = map(int, input().split())

for i in range(n + m):
    arr.append(input())

solution(n, m, arr)
