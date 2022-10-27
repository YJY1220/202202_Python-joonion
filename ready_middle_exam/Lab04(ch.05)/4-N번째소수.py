def is_prime_number(x):
    for i in range(2,x):
        if x % i == 0:
            return False 
    return True 

def solution(num):
    res = 0
    for i in range(1000000):
        if num == 0:
            break
        else:
           if is_prime_number(i) == True:
                res = i
                num-=1
    return res 
        
N = int(input())
print(solution(N))