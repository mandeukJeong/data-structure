def solution(nums):
    answer = 0
    temp = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            temp += 1
        elif nums[i] == 0:
            if answer < temp:
                answer = temp
            temp = 0
    
    if answer < temp:
        answer = temp

    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))
