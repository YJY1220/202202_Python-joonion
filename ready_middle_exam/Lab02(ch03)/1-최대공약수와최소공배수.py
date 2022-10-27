def gcd(N,M):
    if M < 0:
        return 0
    elif M == 0:
        return N
    else:
        return int(gcd(M, N%M))
    
def lcm(N,M):
    return int(N*M / gcd(N,M))

N, M = map(int,input().split())
print(gcd(N,M))
print(lcm(N,M))