def solution(a):
    maximum = 0
    ch = set()
    for i in a:
        if i in ch:
            return 0
        ch.add(i)
        if maximum < i:
            maximum = i
    if len(ch) < maximum:
        return 0
    return 1
