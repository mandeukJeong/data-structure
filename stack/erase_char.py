def solution(s):
    answer = ""
    stack = []
    tmp = ""

    for x in s:
        if x == tmp:
            stack.pop()
            if len(stack) > 0:
                tmp = stack[len(stack) - 1]
            else:
                tmp = ""
        else:
            stack.append(x)
            tmp = x

    answer = ''.join(stack)
            
    return answer

print(solution("acbbcaa"))
print(solution("bacccaba"))
print(solution("aabaababbaa"))
print(solution("bcaacccbaabccabbaa"))
print(solution("cacaabbc"))
