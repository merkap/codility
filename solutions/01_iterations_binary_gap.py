def solution(N):
    x = "{0:b}".format(N)

    max = 0
    count =0
    first = False

    for i in x:
        if i == "0":
            if first:
                count += 1
        else :
            if max < count:
                max = count
            first = True
            count = 0
    print(max)
solution(9)
solution(529)
solution(20)
solution(15)
solution(1041)
