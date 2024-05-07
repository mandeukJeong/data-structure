def solution(nums):
    nums.sort(key = lambda v : (v[0], v[1]))

    return nums

n = int(input())
arr = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

print(solution(arr))