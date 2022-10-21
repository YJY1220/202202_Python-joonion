def find(n):
    maxnum = 0
    index_arr=0
    for i in range(len(n)):
        if(n[i] > maxnum):
            maxnum = n[i]
            index_arr = i
        else:
            maxnum = maxnum
    if(index_arr == 0 or index_arr==len(n)-1):
        print("-1")
    else:
        print(index_arr)
    
num=list()
N = int(input())
for i in range(N):
    num.append(int(input()))
find(num)
      