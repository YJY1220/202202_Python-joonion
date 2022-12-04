# Maze DFS
import sys
sys.setrecursionlimit(10**6)
mind =1000000
count =0
def dfs(i,j,Depth,Maze,Visited,N,M):
  global mind
  global count
  count +=1
  if((i==N-1) and (j==M-1)):
    mind = min(mind,Depth)

  else:
    if(i+1<N and i-1>=0 and j+1 <M and j-1>=0):
      if Maze[i][j] == 1 and Visited[i][j]:
        visit = []
      for y in range(N):
        tem =[]
        for x in range(M):
          tem.append(Visited[y][x])
        visit.append(tem)
      visit[i][j]= False
      dfs(i+1,j,Depth+1,Maze,visit,N,M)
    # if((i+1<N) and (Maze[i+1][j]==1) and (Visited[i+1][j])):
    #   visit = []
    #   for y in range(N):
    #     tem =[]
    #     for x in range(M):
    #       tem.append(Visited[y][x])
    #     visit.append(tem)
    #   visit[i][j]= False
    #   dfs(i+1,j,Depth+1,Maze,visit,N,M)
    # if((j+1<M ) and (Maze[i][j+1]==1)and (Visited[i][j+1])):
    #   visit = []
    #   for y in range(N):
    #     tem =[]
    #     for x in range(M):
    #       tem.append(Visited[y][x])
    #     visit.append(tem)
    #   visit[i][j]= False
    #   dfs(i,j+1,Depth+1,Maze,visit,N,M)
    # if((i-1>=0) and (Maze[i-1][j]==1)and (Visited[i-1][j])):
    #   visit = []
    #   for y in range(N):
    #     tem =[]
    #     for x in range(M):
    #       tem.append(Visited[y][x])
    #     visit.append(tem)
    #   visit[i][j]= False
    #   dfs(i-1,j,Depth+1,Maze,visit,N,M)
    # if((j-1>=0) and (Maze[i][j-1]==1)and (Visited[i][j-1])):
    #   visit = []
    #   for y in range(N):
    #     tem =[]
    #     for x in range(M):
    #       tem.append(Visited[y][x])
    #     visit.append(tem)
    #   visit[i][j]= False
    #   dfs(i,j-1,Depth+1,Maze,visit,N,M)

N, M = map(int,input().split())
Maze = []
for _ in range(N):
  Maze.append(list(map(int,input().split())))

Visited = [[True]* M for _ in range(N)]
dfs(0,0,0,Maze,Visited,N,M)
print(mind)