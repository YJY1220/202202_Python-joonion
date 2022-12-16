def dfs(i,j,matrix,N):
    visited = False
    start = matrix[i][j]
    
    if(i == N -1 and j == N - 1):
        visited = True 
    else:
        if(i+start<=N-1 and j+start<=N-1):
            optionA = dfs(i+start,j,matrix,N)
            optionB = dfs(i,j+start,matrix,N)
            
            if(optionA):
                visited=True 
                return visited 
            else:
                if(optionB):
                    visited = True
                    return visited 
        
        elif(i+start<=N-1):
            visited = dfs(i+start,j,matrix,N)
        elif(j+start<=N-1):
            visited = dfs(i,j+start,matrix,N)
    return visited 

N = int(input())
number_cell = []
for i in range(N):
    cell = list(map(int,input().split()))
    number_cell.append(cell)
     
visited = dfs(0,0,number_cell,N)
if(visited):
    print("Yes")
else:
    print("No")