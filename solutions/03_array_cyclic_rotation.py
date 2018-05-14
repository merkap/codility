def solution(a, k):
    n = len(a)

    if n == 0:
        return a

    k %= n

    if k == 0:
        return a

    return a[n-k:] + a[:n-k]


arr = [
    [3, 8, 9, 7, 6], 1,
    [1, 2, 3, 4], 4,
[3, 8, 9, 7, 6], 3
]
for b, c in zip(arr[0::2], arr[1::2]):
    print(solution(b, c))
