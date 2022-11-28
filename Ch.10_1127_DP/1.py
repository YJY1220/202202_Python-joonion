N = int(input())


def sebonacci(n):
    a=1
    b=2
    c=3
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    else:
        for i in range(4,n+1):
           d = a+b+c
           a = b
           b = c
           c = d
    return d
print(sebonacci(N))