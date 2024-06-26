def solution(box, limit):
    answer = 0
    box.sort(key = lambda v : (-v[1], -v[0]))

    for x in box:
        if limit == 0:
            break

        if limit >= x[0]:
            answer += x[0] * x[1]
            limit -= x[0]
        else:
            answer += limit * x[1]
            limit = 0
               
    return answer
                                           
print(solution([[2, 20], [2, 10], [3, 15], [2, 30]], 5))
print(solution([[1, 50], [2, 20], [3, 30], [2, 31], [5, 25]], 10))
print(solution([[3, 40], [5, 20], [5, 70], [1, 80], [5, 30], [3, 35]], 15))
print(solution([[2, 70], [5, 100], [3, 90], [1, 95]], 8))
print(solution([[80, 20], [50, 10], [70, 15], [70, 30], [80, 70], [90, 88], [70, 75]], 500))

