def find(n,arr):
    index_arr = 0
    max = 0
    for i in range(n):
        if arr[i] > max:
            max = arr[i]
            index_arr = i 
        else:
            max = max
    if(index_arr ==0 or index_arr==n-1):
        print("-1")
    else:
        print(index_arr)

N = int(input())
first = []
for i in range(N):
    num = int(input())
    first.append(num)
find(N,first)
