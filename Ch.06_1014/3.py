# N = int(input())
# for i in range(N):
#     num = int(input())

# def find(N, key):
#     key = int(N[0])
#     for i in range(N):
#         if key == i:
#             return key
#         else:
#             key = N[i+1]
#             return find(N,key)
#     return -1
    
# print(find(N,num))


N = int(input())
list=[]
for i in range(N):
    num = int(input())
    list.append(num)
cnt = 0

for i in range(N):
    if int(list[i]) == i:
        print(i)
        cnt += 1
if cnt == 0:
    print(-1)