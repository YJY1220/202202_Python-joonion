def solve(x):
    if x == 0:
        return 1
    else:
        # res = 1
        # for i in range(1, x+1): #끝 숫자는 연산에 포함 안 됨
        #     res *= i
        # return res
        return x * solve(x-1)

N = int(input())
print(solve(N))