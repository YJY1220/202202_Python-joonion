import sys
sys.setrecursionlimit(10**6)

def Ack(x,y):
    if x == 0:
        return y + 1
    elif x>=0 and y ==0:
        return Ack(x-1, 1)
    else:
        if x>0 and y>0:
            return Ack(x-1, Ack(x,y-1))


N,M = map(int, input().split())
print(Ack(N,M))