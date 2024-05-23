def solution(s):
    answer = "YES"
    stack = []

    for x in s:
        if x == "(":
            stack.append(x)
        else:
            if len(stack) == 0:
                return "NO"
            else:
                stack.pop()

    return answer if len(stack) == 0 else "NO"

print(solution("((()))()"))
print(solution("(()(()"))
print(solution("()())"))
print(solution("())("))
print(solution("((())))()("))
