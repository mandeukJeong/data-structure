def DFS(n):
    if n == 1 or n == 2:
        return 1
    elif n >= 3:
        return DFS(n - 1) + DFS(n - 2)
                  
print(DFS(5))
print(DFS(6))
print(DFS(8))
print(DFS(10))

