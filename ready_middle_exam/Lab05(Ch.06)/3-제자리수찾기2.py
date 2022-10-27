def find(k,n):
    check = 0
    for i in range(n):
        if k[i] == i:
            print(i)
            check += 1
    if(check == 0):
        print("-1")

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    arr.append(num)
find(arr,N)

    