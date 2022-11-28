N = int(input())
stairs = list(map(int,input().split()))

def solve(n, arr):
    max_array = [0] * (n)    
    max_array[0] = arr[0]
    max_array[1] = max(arr[1],arr[1]+max_array[0])
    for i in range(2, n):
        max_array[i] = arr[i] + max(max_array[i-1], max_array[i-2]) 
    
    return max_array[n-1] 

print(solve(N,stairs))
        