def collatz(x):
    if x == 1:
        return [1]
    elif x % 2 == 0:
        return [x] + collatz(x//2)
    else:
        return [x] + collatz(3*x + 1)

A = list()
def compare(A):
    MAX = collatz[1]
    for i in range((len(A))):
        if MAX > A[i]:
            MAX = MAX
        else:
            MAX = A[i]
    return MAX

N = int(input())
print(collatz(N))
print(max(collatz(N)))