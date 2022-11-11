def collatz(x):
    if x==1:
        return [1]
    elif x%2==0:
        return [x] + collatz(x//2)
    else:
        return [x] + collatz(3*x + 1)

#collatz는 저렇게 되면 알아서 배열로 return해줌
#즉, 리턴된 배열값을 담을 list 변수를 하나 만들어줘야함
#collatz(num)이 그 num값 넣은 배열임
def compare(num):
    ll = collatz(num)
    max = ll[0]
    for i in range(len(ll)):
        if max > ll[i]:
            max = max
        else:
            max = ll[i]
    return ll

N = int(input())
#print(collatz(N))
print(compare(N))

#162964
