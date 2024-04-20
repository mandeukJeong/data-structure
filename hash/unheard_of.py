from collections import defaultdict
def solution(n, m, name):
    answer = []
    sH = defaultdict(int)

    for x in name:
        sH[x] += 1
    
    for key in sH:
        if sH[key] == 2:
            answer.append(key)
    
    print(len(answer))
    for x in sorted(answer):
        print(x)
    
arr = []
n, m = map(int, input().split())

for i in range(n + m):
    arr.append(input())

solution(n, m, arr)
