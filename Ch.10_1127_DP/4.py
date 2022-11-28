N,M = map(int,input().split())
maze = [list(map(int,input().split())) for _ in range(N)]

def solve(n,m,maze_arr):
    arr = [[0] * m for _ in range(n)]
    arr[0][0] = maze_arr[0][0]
    for i in range(1,n):
        arr[i][0] = maze_arr[i][0] + arr[i-1][0]
    for j in range(1,m):
        arr[0][j] = maze_arr[0][j] + arr[0][j-1]    
    for i in range(1, n):
        for j in range(1,m):
            arr[i][j] = maze_arr[i][j] + min(arr[i-1][j], arr[i][j-1])
       
    return arr[n-1][m-1]

print(solve(N,M,maze))