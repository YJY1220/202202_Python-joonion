def solution(x,y):
    res = 0
    cnt = 1
    cnt_pre = 0
    res = 0
    for i in range(x,y+1):
        if (i % 4 == 0 and i % 100 != 0) or i % 400 == 0:
            for i in range(366):
                cnt_pre = cnt
                cnt = cnt_pre + 1
                res += cnt             
        else:
            for i in range(365):
                cnt_pre = cnt 
                cnt = cnt_pre + 1
                res += cnt
    return res #전체 for문에 대한 결과값을 리턴해야하므로 return 값은 여기다 적어줘야함
            # return 쓸 때 += 이런거 못씀

X = int(input())
Y = int(input())

print(solution(X,Y))