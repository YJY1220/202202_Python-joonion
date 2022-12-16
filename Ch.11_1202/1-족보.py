N,M = map(int,input().split())
P,Q = map(int,input().split())
graph = [[]for _ in range(N+1)]
visited = [False] * (N+1)
family = []
for i in range(M):
    numP, numQ = map(int,input().split())
    graph[numP].append(numQ)
    graph[numQ].append(numP)
    
def solve(v,cnt):
    cnt += 1
    visited[v] = True
    
    if v == Q:
       family.append(cnt)
       
    for i in graph[v]:
        if not visited[i]:
            solve(i,cnt)
    
solve(P,0)
print(family[0] - 1)

#print(family[0] - 1)
             