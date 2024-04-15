from collections import deque

def solution(nums, k):
    dq = deque()
    answer = []
    
    for i in range(k):
        dq.append(nums[i])
    
    for i in range(len(nums) - 1, k - 1, -1):
        dq.appendleft(nums[i])

    answer = list(dq)
    
    return answer


print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))


