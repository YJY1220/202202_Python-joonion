import sys
input = sys.stdin.readline 

N = input()
arr = input().split()

arr.sort(key = lambda x: (len(x), -int(x)))
    
print(" ".join(arr))