from random import uniform

number = uniform(1,80)

if 1<=number<=16:
    print("마라탕")
elif 17<=number<=35:
    print("김치찌개")
elif 36<=number<=60:
    print("지예가 먼저 씻기")
else:
    print("재미니가 먼저 씻기")
print(number)

# jaeminMind ="대청교가기시러"

# for i in range(100):
#     if(jaeminMind=="대청교가기시러"):
#         print("대청교 가기 시러")
#     else:
#         print("대청교 안가도 돼!")


# import random

# N = 100
# S = list(range(1,N+1))
# random.shuffle(S)
# if(S[0]<=50):
#     print("지예가 먼저 씻습니다.")
# else:
#     print("재민이가 먼저 씻습니다.")
