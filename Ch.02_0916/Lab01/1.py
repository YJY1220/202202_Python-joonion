def solve(x,y):
    res = 0
    for i in range(x,y+1):
        if (i%4 == 0 and i %100!=0) or i%400==0:
            res += 366
        else:
            res += 365
    return res
    
    
year_A = int(input())
year_B = int(input())

print(solve(year_A, year_B))