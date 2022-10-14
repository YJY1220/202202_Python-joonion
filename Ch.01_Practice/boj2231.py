def sumofdigits(n):
    s, t = 0, n #s=0, t=n
    while t>0:
        s += t % 10
        t = t // 10
    return s

def solve(n):
    for m in range(1, n+1):
        if n == m + sumofdigits(m):
            return m
    return 0

# def solve(n):
#     for m in range(1,n+1):
#         if n == m + sum(map(int,str(m))): -> 이 sum,map은 무슨 함수?
#             return m
#     return 0

N = int(input())
print(solve(N))