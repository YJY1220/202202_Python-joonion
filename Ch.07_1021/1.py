def solution(x,y,z):
    for i in range(L):
        for j in range(N):
            for k in range(M):
                z[i][j] += x[i][k] * y[k][j]
    for i in range(len(z)):
        for j in range(len(z[i])):
            if(j==len(z[i])-1):
                print(z[i][j])
            else:
                print(z[i][j], end=' ')
        
L,M,N = map(int, input().split())
A=list()
B=list()
C=list()
for i in range(L):
    A.append(list(map(int,input().split())))
for j in range(M):
    B.append(list(map(int,input().split())))
# for _ in range(L):
#     C = [0 for _ in range(N)]
C=[[0 for _ in range(N)] for _ in range(L)]
solution(A,B,C)

