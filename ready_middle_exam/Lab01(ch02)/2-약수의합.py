def solution(num):
    res = 0
    for i in range(1,num+1):
        if num % i == 0:
            res += i
    return res

N = int(input())
print(solution(N))