from re import I


num = int(input())

sum = 0
for i in range(1,int(num**0.5)+1):
    if(num%i==0):
        sum += i
        if(num/i != i):
            sum += (num//i)

print(sum)