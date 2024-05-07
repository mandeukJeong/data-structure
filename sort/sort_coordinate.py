def solution(nums):
    nums.sort(key = lambda v : (v[0], v[1]))
    for x in nums:
        print(x[0], x[1])


n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])
solution(arr)