n = input()
arr = input().split()

def Judge(N,M):
    # for i in range(len(M)):
    #     for j in range(len(N)):
    #         if(N[j] == M[i]):
    #             break
    #         if(N[j] != M[i] and j==len(N)-1):
    #             return False
    # return True
    for i in range(len(N)):
        for j in range(len(M)):
            if(M[j] == N[i]):
                break
            if(M[j] != N[i] and j==len(N)-1):
                return False
    return True
    

def solution(n,arr):
    cnt = 0
    for i in range(len(arr)):
        if(Judge(n,arr[i]) == True):
            cnt += 1
    return cnt

print(solution(n,arr))     
    
