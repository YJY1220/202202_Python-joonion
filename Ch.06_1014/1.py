def find(x,low,high):
    if low > high:
        return x, -1
    else:
        mid = (low+high) // 2
        if x == mid:
            print(x, "END")
        elif x < mid:
            print(mid, "DOWN")
            find(x, low, mid -1)
        else:
            print(mid, "UP")
            find(x,mid+1, high)

N,M = map(int, input().split())
num = int(input())
find(num, N, M)