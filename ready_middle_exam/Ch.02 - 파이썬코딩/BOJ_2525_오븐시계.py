def solution(n):
    sum = 0
    res = 0
    for i in range(len(n)):
        sum += n[i] * n[i]
    sum %= 10
    print(sum)
    return 0 

num = []
num = list(map(int,input().split()))
solution(num)

       
       