# #반복 - 순차탐색
# S = list(map(int,input().split()))

# def seqsearch(S, x):
#     for i in range(len(S)):
#         if x == S[i]:
#             return S[i], i
#     return x, -1

# print(seqsearch(S, 53))

# K,N = map(int, input().split())
# for i in range(len(N)):
#     numStand = input()

# global cnt  

# def divide(K,N, low, high):
#     low, high = 0, len(K) -1
#     if(low>high) :
#         return N, -1
#     else:
#         mid = (low+high) // 2
#         if N == K[mid]:
#             cnt += 1
#             return K[mid], mid
#         elif N < K[mid]:
#             return divide(K,N,low, mid-1)
#         else:
#             return divide(K,N,mid+1, high)
        
# print(cnt)

# BOJ 1654 랜선자르기
def possible(mid, A):
    cnt = 0
    for i in range(len(A)):
        cnt += A[i] // mid
    return cnt

def binsearch(n,A,low,high):
    if low>high:
        return high
    else:
        mid = (low+high)//2
        maxn = possible(mid, A)        
        if n <= maxn:
            return binsearch(n,A,low,mid-1)
        else:
            return binsearch(n, A, mid+1, high)
            
        
def solve(n,A):
    return binsearch(n,A,1,max(A))

K, N = map(int,input().split())
A = [int(input()) for _ in range(K)]
print(K,N,A)
