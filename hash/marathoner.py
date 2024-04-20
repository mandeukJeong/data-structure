from collections import defaultdict, Counter
def solution(participant, completion):
    answer = ''
    sH = defaultdict(int)

    for x in participant:
        sH[x] += 1

    for x in completion:
        sH[x] += 1

    sH = Counter(sH)

    for key in sH:
        if sH[key] % 2 != 0:
            answer = key
            
    return answer


n = int(input())
a = []

for i in range(n):
    a.append(input())

b = []

for i in range(n - 1):
    b.append(input())

print(solution(a, b))