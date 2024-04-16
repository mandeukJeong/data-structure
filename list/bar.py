def solution(sticks):
    print(sticks)
    answer = []

    for i in range(len(sticks) - 1):
        if sticks[i] > sticks[len(sticks) - 1] and sticks[i] not in answer:
            answer.append(sticks[i])
   
    return len(answer) + 1


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

print(solution(arr))