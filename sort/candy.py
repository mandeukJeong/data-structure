def solution(nums):
    answer = 0
    tmp = 0
    nums.sort()
    pos = len(nums) // 2

    for x in nums:
        if x != tmp:
            tmp = x
            answer += 1

    if pos < answer:
        answer = pos
            
    return answer
    
                       
print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))
