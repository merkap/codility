def solution(a):
    count = 0
    multiply = 0
    for car in a:
        if car == 0:
            multiply += 1
        if multiply > 0:
            if car == 1:
                count += multiply
                if count > 1000000000:
                    return -1
    return count
