def solution(nums):
    answer = 0
    tmp = False
    stack = []

    for x in nums:
        if x == 1:
            if tmp:
                stack.pop()
                stack.pop()
                answer += 1
                tmp = False
            else:
                stack.append(x)
        else:
            if len(stack) > 0 and stack[len(stack) - 1] == 1:
                tmp = True
            else:
                tmp = False
            stack.append(x)

    return answer
    
print(solution([1, 1, 1, 2, 1, 1, 2, 1, 2, 1]))
print(solution([2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 2, 1, 2, 1, 2, 1]))
print(solution([1, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1]))
print(solution([2, 1, 1, 1, 2, 1, 2]))
print(solution([1, 1, 1, 1, 1, 1, 1]))
