def solution(a,b):
    sum = 0
    minimum = b*b
    for i in range(1,b):
        if i*i >= a and i*i<=b:
           sum += i*i
           if minimum >= i*i:
               minimum = i*i
           else:
               minimum = minimum     
    if(sum==0):
        print(-1)
    else:
        print(sum)
        print(minimum)

M = int(input())
N = int(input())
solution(M,N)

             
