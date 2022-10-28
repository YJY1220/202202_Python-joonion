def calculate(a,b,l,m,n):
    C = [[0]*l for _ in range(n)]
    for i in range(l):
        for j in range(m):
            for k in range(n):
                C[i][k] += a[i][j] * b[j][k]
    return C 

L,M,N = list(map(int,input().split()))
A = [list(map(int,input().split())) for _ in range(L)]
B = [list(map(int,input().split())) for _ in range(M)]

res = calculate(A,B,L,M,N)

for i in range(L):
    print(" ".join(map(str,res[i])))