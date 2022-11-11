# def divide(x, y, n):
#     check = array[x][y]
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if check != array[i][j]:
#                 check = -1
#                 break

#     if check == -1:
#         print("Q", end='')
#         n = n // 2
#         divide(x, y, n)  
#         divide(x, y + n, n)  
#         divide(x + n, y, n)  
#         divide(x + n, y + n, n)  

#     elif check == 1:
#         print('B',end='')
#     else:
#         print('W',end='')
        
# N = int(input())
# array = [list(map(int, input().split())) for _ in range(N)]
# print(N)
# divide(0, 0, N)
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]


def dnc(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                check = -1
                break

    if check == -1:
        print("Q", end='')
        n = n // 2
        dnc(x, y, n)  # 오른쪽 위
        dnc(x, y + n, n)  # 왼쪽 위
        dnc(x + n, y, n)  # 오른쪽 아래
        dnc(x + n, y + n, n)  # 왼쪽 아래

    elif check == 1:
        print('B',end='')
    else:
        print('W',end='')

print(n)
dnc(0, 0, n)