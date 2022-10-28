N =int(input())
def calculate(n,a,m,k):
    resarray = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                resarray[i][k] += a[i][j] * a[j][k]
            resarray[i][k] = resarray[i][k] % m 
    return resarray  

def power(n,a,m,k):
    if k == 1:
        return a 
    multi = power(n,a,m,k//2)
    if k % 2 == 0:
        return calculate(n,multi,multi,k)
    else:
        return calculate(n,a,calculate(n,multi,multi),k)

A=[list(map(int,input().split())) for _ in range(N)]
M,K = map(int,input().split())
res = power(N,A,M,K)
for i in range(N):
    print(" ".join(map(str,res[i])))
