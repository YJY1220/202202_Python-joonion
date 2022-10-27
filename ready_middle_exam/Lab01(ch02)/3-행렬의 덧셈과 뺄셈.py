def solve(n,m,a,b,c):
    resArray = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            resArray[i][j] = a[i][j] + b[i][j] - c[i][j]
    return resArray

N,M = map(int,input().split())

A=[]
A = list(map(int,input().split()) for _ in range(N))
B=[]
B = list(map(int,input().split()) for _ in range(N))
C=[]
C = list(map(int,input().split()) for _ in range(N))
resArray = solve(N,M,A,B,C) #그냥 리스트하나만 받으면 됨 이렇게 [i][j] 이런거 필요없음
for i in range(N):
    print(" ".join(map(str,resArray[i]))) #여기 왜 str로 입력받지?