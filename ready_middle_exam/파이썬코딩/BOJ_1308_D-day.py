def judge_year(year,month,day):
    if year%4==0 and year%100!=0:
        if year%400==0:
            return 366
    else:
        return 365


sy,sm,sd = map(int,input().split())
ey,em,ed = map(int,input().split())

sum = 0
if ey-sy>0:
    for i in range()
else:
    if em-sm>0:     