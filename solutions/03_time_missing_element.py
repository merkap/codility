def solution(a):
    length = len(a)
    prog_sum = int((2 + length) / 2 * (length+1))
    for i in a:
        prog_sum -= i
    return prog_sum
