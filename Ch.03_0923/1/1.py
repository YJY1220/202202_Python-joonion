def gcd(a,b):
    if b == 0:
        return a
    else: 
        if b>0:
           return gcd(b, a % b)
    
def lcm(x,y):
    return int(x * y / gcd(x,y))

num1, num2 = map(int,input().split())
print(gcd(num1,num2))
print(lcm(num1,num2))
