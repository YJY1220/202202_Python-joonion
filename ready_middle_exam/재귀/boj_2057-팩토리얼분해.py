N = int(input())

def factorial(num):
    if num == 0 :
        return 1
    else:
        return num * factorial(num-1)
    
def solution(n):
    if N > factorial(N-1):
        check += 1
        return solution(n)
    