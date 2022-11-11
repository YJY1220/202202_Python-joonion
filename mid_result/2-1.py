def perm(n,r):
    #종료
    if r == 0:
        return 1
    #재귀
    else:
        return n*perm(n-1,r-1)
           
n, r= 1234567, 890
print(perm(n,r)) 