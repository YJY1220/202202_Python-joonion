# def  Roman2Number(roman):
#     rdict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     nv = roman[0]
#     number=rdict[nv]
#     for i in range(1,len(roman)):
#         bv = nv
#         nv = roman[i]
#         if(rdict[bv]>=rdict[nv]):
#             number += rdict[nv]
#         else:
#             number += rdict[nv] - 2*rdict[bv]
#     return number
# print("%d"%Roman2Number("CXCIX"))

# def is_prime(num):
#     root = int(num ** 0.5 + 1)
#     for i in range(2,root):
#         if num % i == 0:
#             return False
        
#     return True

# n = int(input())
# print(is_prime(n))

# from string import ascii_lowercase
# import random
# random.seed(1234)
# for i in range(100):
#     S = "".join(random.sample(ascii_lowercase[:7], 5))
#     print(S)

# import random
# random.seed(1234)
# N = 100
# S = random.sample(range(-100,100),N)
# print(" ".join(map(str,S)))

# import random
# random.seed(1234)
# N = 1000
# S = [0]*(N+1)
# for i in range(2,N+1):
#     S[i] = random.randint(1,i-1)
# T = {i:[] for i in range(1,N+1)}
# for i in range(2,N+1):
#     T[S[i]].append(i)
# for key in T.keys():
#     for value in T[key]:
#         print(key,value)

import random
random.seed(1234)
N = 5
for i in range(120):
    S = [j for j in range(1,N+1)]
    random.shuffle(S)
    print(S)