# print(input().split()) #split은 list 자료형
# a, b = map(int, input().split()) #int는 자료형, map앞에 list 안적어도 나란히 입력 가능                                 
#                                  #map은 list의 요소를 지정된 함수로 바꾸어주는 것
#                                  #list붙이고 안 붙이고의 차이는 그다지 나지 않음 -> input().split()를 list로 받기 때문, tuple로 받으면 map 앞에 tuple임.

def time(H,M):
    if M >= 45:
        M = M-45
    else:
        M = (M-45) % 60 
        H = (H-1) % 24
    return H,M

HV, MV= map(int, input().split()) 
H, M = time(HV, MV)
print(H,M)
