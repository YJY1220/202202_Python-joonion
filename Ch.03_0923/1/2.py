def gcd(a,b):
    if b == 0:
        return a
    else: 
        if b>0:
           return gcd(b, a % b)
    
def lcm(x,y):
    return int(x * y / gcd(x,y))

num = list()
N = int(input())

num = list(map(int, input().split()))
temp = num[0]
for i in range(0,N):
    temp=lcm(temp,num[i])
    
print(int(temp))
