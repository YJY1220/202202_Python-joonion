N = int(input())
x = {}
y = {}

for i in range(N):
    xNum, yNum = map(int,input().split())
    #x인경우
    if xNum in x.keys() :
        x[xNum] += 1
    else:
        x[xNum] = 1
    #y인경우
    if yNum in y.keys():
        y[yNum] += 1
    else:
        y[yNum] = 1

xcount = 0
ycount = 0

for i in x.keys():
    if(x[i] >= 2):
        xcount += 1
for i in y.keys():
    if(y[i] >= 2):
        ycount += 1

print(xcount)
print(ycount)