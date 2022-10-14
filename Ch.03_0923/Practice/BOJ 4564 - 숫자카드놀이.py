def solve(x):
    print(x, end = " ") #한줄로 출력할 때 
    s = str(x)
    if len(s) == 1:
        return s
    else:
        res = 1
        for i in range(len(s)):
            res *= int(s[i])
        return solve(res)
A = list()

while(True):
    N = int(input())
    if N==0:
        break
    else:
        A.append(N)

for i in range(len(A)):
    solve(A[i])
    print() 
