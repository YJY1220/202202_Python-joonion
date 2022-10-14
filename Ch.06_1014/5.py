def is_Prime():
    N = 5000000
    a = [False,False] + [True]*(N-1)
    p=[]
    for i in range(2,N+1):
        if a[i]:
            p.append(i)
            for j in range(2*i, N+1, i):
                a[j] = False
    return p
        
def solve(n,p):
    high = len(p)
    low = 0
    while(low <= high):
        mid = (low + high) // 2
        if(p[mid] == n):
            return mid + 1
        elif(p[mid] < n):
            low = mid + 1
        else:
            high = mid - 1
    return -1

N=int(input())
p = is_Prime()
for i in range(N):
    num = int(input())
    print(solve(num, p))