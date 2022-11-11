def Compf(x,y):
    if x>=y:
        min_x=y
        max_y=x
    else:
        min_x=x
        max_y=y
    return min_x,max_y

def Sumf(n,m):
    sum=0
    for i in range(n,m+1):
        sum+=i 
    return sum 

n = int(input())
m = int(input())

min,max = Compf(n,m)
result=Sumf(min,max)
print(result)