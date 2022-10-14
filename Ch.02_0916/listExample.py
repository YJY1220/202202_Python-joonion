#lamda는 익명함수임 -> 임의의 함수

x = [1,3,5,7,9, "hello"] # list형식임
for i in range (len(x)): #x길이로 그냥 바로 출력
    print(i, end= " ")
print()
for i in range(len(x)):
    print(x[i], end=" ")
print()
for i in x:
    print(i) #x[i]인데 x안에 있는 i를 그냥 바로 출력
print()
#제곱 출력
# for i in range(len(x)):
#     print(x[i]**2, end=" ")