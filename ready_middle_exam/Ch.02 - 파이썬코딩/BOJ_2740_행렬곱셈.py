def solution(a,b,n,m,k):
    res =[[0] * k for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for t in range(k):
              res[i][t] += a[i][j] * b[j][t]
    return res

N, M = map(int,input().split())
arrayA = [list(map(int,input().split())) for _ in range(N)]
M, K = map(int,input().split())
arrayB = [list(map(int,input().split())) for _ in range(M)]
ans = solution(arrayA,arrayB,N,M,K)
for i in range(N):
    for j in range(K):
        print(ans[i][j], end=" ")
    print()
    
    

