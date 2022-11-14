def solve(num,arr):
    store = []
    for i in range(num):
        while(len(store) != 0 and store[-1] <= arr[i]):
            store.pop()
        store.append(arr[i])
    return store

N = int(input())
arr = list(map(int,input().split()))
print(" ".join(map(str,solve(N,arr))))
        