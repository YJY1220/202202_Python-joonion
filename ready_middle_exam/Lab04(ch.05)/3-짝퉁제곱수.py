def judge(n):
    sum = 0
    while(n//10!=0):
        n = n%10
        sum += n 
        n = n//10 
    sum+=n
     
    if(int(sum**0.5) == sum**0.5):
        return True
    else:
        return False 

def solution(n,m):
    cnt = 0
    for i in range(n,m+1):
        if(judge(i) == True):
           cnt += 1
    return cnt  

N,M = map(int,input().split())
print(solution(N,M))



        
        
        