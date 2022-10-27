def gcd(N,M):
    if M < 0:
        return 0
    elif M == 0:
        return N
    else:
        return int(gcd(M, N%M))
    
def lcm(N,M):
    return int(N*M / gcd(N,M))

N = int(input())
num = list(map(int,input().split()))

#이거 논리 이해 잘 안감
temp = num[0]
for i in range(0,N):
    temp=lcm(temp,num[i])

print((int(temp)))