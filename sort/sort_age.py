def solution(member):
    member.sort(key = lambda v : v[0])
    
    for x in member:
        print(x[0], x[1])

n = int(input())
arr = []

for i in range(n):
    a, b = input().split()
    a = int(a)
    arr.append([a, b])

solution(arr)
