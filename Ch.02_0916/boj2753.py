def solve(x): #파라미터만 나열해주면 알아서 type 지정? 이게 뭔솔
    if (x % 4 == 0 and x % 100 != 0) or x % 400 == 0:
        return 1  #def 같은 건 문장 끝날 때 : 지정해주면 됨
                     #들여쓰기로 블락지정
    else:
        return 0
    
year = int(input()) #입력받은 문자열 (input())을 int 정수형 type으로 변환
print(solve(year))
    