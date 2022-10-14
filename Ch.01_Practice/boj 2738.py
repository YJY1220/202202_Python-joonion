def solve(n,m,A,B):
    C = [[0] * m for _ in range(n)] #[0]얘는 갑자기 왜 튀어나옴?
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] + B[i][j]
    return C

N,M = map(int, input().split()) #옆으로 나란히 입력받는거?
A = [list(map(int, input().split())) for _ in range(N)] #이렇게 for 다음에 _ 띄어서 적는 이유는?
B = [list(map(int, input().split())) for _ in range(N)]
C = solve(N,M,A,B)

for i in range(N):
    print(" ".join(map(str,C[i]))) #join은 무엇?