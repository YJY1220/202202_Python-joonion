def find(key,low,high):
    while low <= high:
        mid = (low+high) // 2
        if key == mid:
            print(key)
            print("END")
            break
        elif key < mid:
            print("DOWN")
        else:
            print("UP")
    return 0

N,M = map(int,input().split())
X = int(input())
find(X,N,M)

   
    