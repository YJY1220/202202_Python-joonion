import sys
input = sys.stdin.readline

N = int(input())    
num = list()

num = input().split()
num.sort(key = lambda x : (len(x), -int(x))) 

print(" ".join(num))
    
 

