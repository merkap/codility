def solution(a):
    head = a[0]
    tail = sum(a[1:])
    min_dif = abs(head - tail)

    for index in range(1, len(a) - 1):
        head += a[index]
        tail -= a[index]
        if abs(head - tail) < min_dif:
            min_dif = abs(head - tail)

    return min_dif
