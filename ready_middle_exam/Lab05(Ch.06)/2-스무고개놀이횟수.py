def find(key,low,high):
    cnt = 1
    while low<=high:
        mid = (low+high)//2
        if key == mid:
            cnt = cnt 
            break 
        elif key<mid:
            cnt += 1
            high = mid - 1 
        else:
            cnt +=1 
            low = mid + 1
    return cnt 

N,M = map(int,input().split())
K = int(input())
X = list(map(int,input().split()))
sum = 0
for i in range(K):
    sum += find(X[i], N, M)
print(sum)

