def judge(n,m):
    for i in range(len(n)):
        for j in range(len(m)):
            if n[i] == m[j]:
                break
            if n[i] != m[j] and j == (len(n) - 1):
                return False
    return True
def solution(n,m):
    cnt = 0
    for i in range(len(m)):
        if judge(n,m[i]) == True:
            cnt += 1
    return cnt 

N = input()
arr = input().split()
print(solution(N,arr))                