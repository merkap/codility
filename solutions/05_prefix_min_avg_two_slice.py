def solution(a):
    min_aver = average(a[:2])
    min_ind = 0
    for i in range(0, len(a) - 1):
        for j in range(i + 2, i + 4):
            next_aver = average(a[i:j])
            if next_aver < min_aver:
                min_aver = next_aver
                min_ind = i
    return min_ind


def average(b):
    return sum(b) / len(b)


print(solution([4, 2, 2, 5, 1, 5, 8]))
