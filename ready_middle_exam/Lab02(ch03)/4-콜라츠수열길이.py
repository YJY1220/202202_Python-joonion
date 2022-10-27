def collatz(x):
    if x==1:
        return [1]
    elif x%2==0:
        return [x] + collatz(x//2)
    else:
        return [x] + collatz(3*x + 1)


def compare(num):
    ll = collatz(num)
    max = ll[0]
    for i in range(len(ll)):
        if max > ll[i]:
            max = max
        else:
            max = ll[i]
    return max

N = int(input())
#print(collatz(N))
print(compare(N))