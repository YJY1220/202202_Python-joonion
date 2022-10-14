#ver.1.
def solve(n,low,high):
    global F
    while low<=high:
        mid = (low+high)//2
        if n == F[mid]:
            return mid
        elif n < F[mid]:
            high = mid -1
        else:
            low = mid + 1
    return -1

#ver.2
# def solve(n,low,high):
#     global F 
#     mid = (low+high) // 2
#     if(F[mid] == n):
#         return mid
#     elif(low > high):
#         return -1
#     else:
#         if(F[mid] < n):
#             return solve(n,mid+1,high)
#         else:
#             return solve(n,low, mid-1)

F = list()
F.append(0)
F.append(1)
F.append(1)
for i in range(3,50001):
    F.append(F[i-1] + F[i-2])
        
T = int(input())
for i in range(T):
    num = int(input())
    print(solve(num,1,50000))