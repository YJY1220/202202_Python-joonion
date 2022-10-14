N,M = map(int,input().split())

def solution(N,M):
    count = 0
    MAX = 0
    MAX_int = 0
    for i in range(N,M+1):
        count = 0
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                count+= 2
                if j==(i/j):
                    count-=1
        if(count>=MAX):
            MAX = count
            MAX_int = i
    print(MAX_int)
    print(MAX)
    
solution(N,M)