N= int(input())
cnt = [0] * 9999999

cnt[1] = 0
cnt[2] = 1
cnt[3] = 1

def solve(n):
    for i in range(4, n+1):
        if i % 3 ==0 and i%2==0:
            cnt[i] = 1 + min(cnt[i//3],cnt[i//2],cnt[i-1])
        elif i % 3 == 0:
            cnt[i] = 1 + min(cnt[i//3],cnt[i-1])
        elif i%2 == 0:
            cnt[i] = 1 + min(cnt[i//2], cnt[i-1])
        else:
            cnt[i] = 1 + cnt[i-1]
    return cnt[n]

print(solve(N))
        