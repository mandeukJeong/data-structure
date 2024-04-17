from collections import Counter
def solution(s):
    answer = 0
    cnt = Counter(s)
    odd = 0
    
    for key in cnt:
        if cnt[key] % 2 == 0:
            answer += cnt[key]
        else:
            answer += cnt[key] - 1
            odd += 1

    return answer + 1 if odd > 0 else answer
                   
print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))
