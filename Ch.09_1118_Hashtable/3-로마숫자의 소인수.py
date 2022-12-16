#참조 함수
def primeNum(N):
  a = [False,False] + [True]*(N-1)
  prime_number= []
  for i in range(2,N+1):
    if a[i]:
      prime_number.append(i)
      for j in range(2*i, N+1, i):
          a[j] = False
  return prime_number

def Change(num): 
  res = 0
  Roman ={'I' : 1, 'V':5, 'X': 10, 'L':50, 'C':100, 'D': 500, 'M':1000}
  for i in range(len(num)):
    if i<len(num)-1 and Roman[num[i]]<Roman[num[i+1]]:
      res -= Roman[num[i]]
    else:
      res += Roman[num[i]]
  
  return res

def Roman(n):
  T ={1000:"M", 900:"CM",500:"D",400:"CD", 100:"C",90:"XC",  50:"L",40:"XL",  10:"X",9:"IX", 5:"V", 4:"IV" ,1:"I"}
  nums=list(T.keys())
  strs= list(T.values())
  r=""
  for i in range(len(T)):
    while n >= nums[i]:
      r+=strs[i]
      n-=nums[i]
  return r

num = input()
num = Change(num)
prime_number = primeNum(5000)
store = []

while(num>1):
    for i in range(len(prime_number)):
        if num % prime_number[i] == 0:
            num //= prime_number[i]
            store.append(prime_number[i]) 
            break 

for i in range(len(store)):
    print(Roman(store[i]))          

