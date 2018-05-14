def solution(s, p, q):
    impact = {
        "A": 1,
        "C": 2,
        "G": 3,
        "T": 4
    }
    result = []
    for i in range(len(p)):
        s += " "
        sub = s[p[i]:q[i]+1]
        if sub.__contains__("A"):
            result.append(impact["A"])
            continue
        if sub.__contains__("C"):
            result.append(impact["C"])
            continue
        if sub.__contains__("G"):
            result.append(impact["G"])
            continue
        if sub.__contains__("T"):
            result.append(impact["T"])
            continue
    return result


print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]))
