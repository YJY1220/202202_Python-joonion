idx = -1

def get_next(s):
    global idx
    idx += 1 
    return s[idx]


cnt = 0
def conquer(i,j,n,s,T):
    head = get_next(s)
    global cnt     
    if head == "W" or head == "B":
        for r in range(i,i+n):
            for c in range(j,j+n):
                if head == "W":
                    T[r][c] = 0
                else:
                    T[r][c] = 1
                    cnt += 1    
    else:
        m = n//2
        conquer(i,j,m,s,T)
        conquer(i,j+m,m,s,T)
        conquer(i+m, j,m,s,T)
        conquer(i+m,j+m,m,s,T)
        
N = int(input())
string_a = input().strip()
array = [[0]*N for _ in range(N)]
conquer(0,0,N,string_a,array)

for i in range(N):
    for j in range(N):
        if(j==len(array[i])-1):
            print(array[i][j])
        else:
            print(array[i][j], end ='')
print(cnt)