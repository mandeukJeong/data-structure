from collections import deque
def solution(nums):
    tmp = 0
    dq = deque()

    for x in nums:
        dq.append(x)
    
    while True:
        if len(dq) == 1:
            return dq[0]
        if tmp < 2:
            dq.popleft()
            tmp += 1
        else:
            dq.append(dq.popleft())
            tmp = 0
            
print(solution([3, 1, 4, 5, 2, 6, 7]))
print(solution([10, 8, 3, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 11, 12, 1, 4, 5, 2, 6, 7, 9]))
print(solution([10, 8, 3, 1, 4, 5, 2, 11, 13, 6, 7, 12, 9, 14]))
print(solution([1, 8, 6, 10, 4, 7, 2, 5, 3, 9]))
