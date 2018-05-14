def solution(n, a):
    result = [0 for i in range(n)]
    last_maximum = 0
    maximum = 0
    for i in range(len(a)):
        a[i] -= 1
        if a[i] >= n:
            last_maximum = maximum
        else:
            result[a[i]] = max(result[a[i]], last_maximum)
            result[a[i]] += 1
            maximum = max(maximum, result[a[i]])
    for i in range(n):
        result[i] = max(result[i], last_maximum)
    return result


print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
