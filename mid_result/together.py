# #철사가 Ncm 있는데, 이를 삼각형으로 만들려면 나올 수 있는 경우의 수는 얼만큼?
# def solve(n):
#     cnt = 0
#     for a in range(1,n):
#         for b in range(a,n):
#             c=n-a-b 
#             if a+b+c ==n and a+b>c:
#                 cnt += 1
#     return cnt 

# N = int(input())
# print(solve(N))

n = int(input())
cnt = 0
# for x in range((n+1)//3, (n+1)//2):
#     for y in range((n-x+1)//2, x+1):
#         cnt += 1
# print(cnt)

for x in range((n+1)//3, (n+1)//2):
    cnt += x-(n-x+1) // 2+1
print(cnt)

#1에서 n까지의 자연수가 있다. 중복은 없다. 그런데, 한 개를 잊어버렸다. 몇 번인지 찾는 방법은?
#카데인 앍도리즘(부분배열의 합 찾기)