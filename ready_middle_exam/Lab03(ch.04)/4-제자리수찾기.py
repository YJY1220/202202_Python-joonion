def solution(n,num):
    global cnt 
    cnt = 0
    for i in range(n):
        if num[i] == i+1:
            cnt += 1
            res.append(int(num[i]))
    return cnt

N = int(input())
arr = list(map(int,input().split()))
res = []
print(solution(N,arr))
for i in range(cnt):
    print(res[i], end=" ")
