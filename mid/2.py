def fac(n):
    fact = 1
    for i in range(1,n+1):
        fact += i
    return fact 

def nCr(n,r):
    return fac(n) / (fac(r) * fac(n-r))

print(nCr(1234567,890)) 