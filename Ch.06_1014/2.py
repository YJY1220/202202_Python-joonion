def find(x,low,high):
    cnt = 1
    while low <= high:
        mid = (low+high) // 2
        if x == mid:
            return cnt
        elif x < mid:
            cnt += 1
            high = mid -1
        else:
            cnt += 1
            low = mid + 1
            
N,M = map(int, input().split())
num = int(input())
ans = list(map(int,input().split()))
cnt = 0

for i in range(len(ans)):
    cnt += find(ans[i], N, M)

print(cnt)