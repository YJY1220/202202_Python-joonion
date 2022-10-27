#python의 재귀호출 횟수 문제
import sys
sys.setrecursionlimit(10**6)

def solution(n,m):
    if n == 0:
        return m + 1
    # else:
    #     if n>0:
    #         if m == 0:
    #             return solution(n-1,1)
    #         else:
    #             if m > 0:
    #                 return solution(n-1, solution(n,m-1))
    elif n>0 and m ==0:
        return solution(n-1,1)
    else:
        if n>0 and m>0:
            return solution(n-1,solution(n,m-1))

n,m = map(int,input().split())
print(solution(n,m))