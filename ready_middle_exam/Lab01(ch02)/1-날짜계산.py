def solution(x,y):
    res = 0
    for i in range(x,y+1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            res += 366
        else:
            res += 365
    return res

X = int(input())
Y = int(input())

print(solution(X,Y))