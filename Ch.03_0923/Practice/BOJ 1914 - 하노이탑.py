cnt = 0

def hanoi(x, str, fin, mid):
    if(x <= 20):
        if(x == 1):
           cnt += 1
           print(str, '->', fin)
        
        else:
            hanoi(x - 1, str, mid, fin)
            cnt += 1
            print(str, '->', mid)
            hanoi(x - 1, mid, fin, str)
            cnt += 1
        return cnt 
    else:
        if(x==1):
            cnt += 1
        else:
            cnt += 2   
        return cnt
    
N = int(input())

hanoi(N,'1','3','2')
print(cnt)
