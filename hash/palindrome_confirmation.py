from collections import Counter
def solution(s):
    answer = False
    cnt = Counter(s)
    odd = 0
    even = 0
    
    for key in cnt:
        if cnt[key] % 2 == 0:
            even += 1
        else:
            odd += 1

    return answer if odd != 1 else not answer
                      
print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))

