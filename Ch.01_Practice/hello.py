#input은 문자열로 넘김 -> 정수형:int(input()) 으로 해야함  

def solve(n,m):
    s = 0
    for i in range(n,m+1):
        s += i
    return s

M,N =map(int,input().split())
S = solve(N,M)
print(S)
