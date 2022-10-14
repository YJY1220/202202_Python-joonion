N = int(input())
M = list(map(int, input().split()))
temp = list()
cnt = 0
    
for i in range(N):
    if M[i] == i+1:
        temp.append(int(M[i]))
        cnt = cnt +1
    
    
print(cnt)
for i in range(cnt):
    print(temp[i], end=" ")