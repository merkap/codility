def solution(a, b, k):
    count = 0
    if a % k == 0:
        count += 1
    return int(b / k) - int(a / k) + count
