def solution(sticks):
    answer = 1
    maxN = sticks[-1]

    for i in range(len(sticks) - 2, -1, -1):
        if sticks[i] > maxN:
            maxN = sticks[i]
            answer += 1
    
    return answer

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(solution(arr))