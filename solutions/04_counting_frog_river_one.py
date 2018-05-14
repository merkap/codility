def solution(x, a):
    s = set(range(1, x+1))
    for i in range(len(a)):
        s.discard(a[i])
        if not s:
            return i
    return -1


print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
