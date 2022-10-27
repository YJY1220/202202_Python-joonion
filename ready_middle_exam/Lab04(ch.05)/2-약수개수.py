def is_Prime_number(k):
    cnt = 1
    for i in range(1,k+1):
        if k%i != 0:
            cnt += 1
        else:
            cnt = cnt 
    return cnt 

def solution(n,m):
    temp = 0
    max = is_Prime_number(n)
    for i in range(n,m+1):
        if max> is_Prime_number(i):
            temp = n
            max = max
        else:
            temp = i
            max = is_Prime_number(i)        
    return temp         


N,M = map(int,input().split())
print(solution(N,M))
print(is_Prime_number(solution(N,M)))