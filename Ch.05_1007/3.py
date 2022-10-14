def judge(k):
    sum = 0
    while(k//10 != 0):
        sum += k%10
        k= k//10
    sum += k
    
    if(int(sum**0.5)==sum**0.5):
        return True 
    else:
        return False

def solution(N,M):
    cnt = 0
    for i in range(N,M+1):
        if(judge(i)):
            cnt+=1
    print(cnt)
    
N,M = map(int,input().split())
solution(N,M)

