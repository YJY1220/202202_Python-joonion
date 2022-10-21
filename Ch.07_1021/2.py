def solution(x,y,z):
    C=[[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(x)):
        for j in range(len(x)):
            for k in range(len(x)):
                C[i][j] += x[i][k] * y[k][j]
            C[i][j] = C[i][j] % z
    return C

def multiply(a,e,k):
    if(e==1):
        return a 
    tempnum = multiply(a,e//2,k)
    if(e%2==0):
        return solution(tempnum,tempnum,k)
    else:
        return solution(a, solution(tempnum,tempnum,k),k) 
      
N = int(input())
A=list()
for i in range(N):
    A.append(list(map(int,input().split())))


M,P = map(int,input().split())
res = multiply(A,P,M)
for i in range(N):
    print(" ".join(map(str,res[i])))