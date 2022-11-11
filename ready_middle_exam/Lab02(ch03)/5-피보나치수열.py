res = 0
def fibo(n):
    if (n==1):
        return 1
    if (n==2):
        return 2
    if (n==3):
        return 3
    else:
        for i in range(4,n):
            res = fibo(i-3) + 2*fibo(i-2) - fibo(i-1)
        return res 

N = int(input())
print(fibo(N))    