def time(H,M):
    if M >= 45:
        M = M-45
    else:
        M = (M-45) % 60 # 왜 60 나머지? 만약 20이면 (-25)%60인데 양수로 되나?
        H = (H-1) % 24
    return H,M

HV, MV= map(int, input().split()) #map의 기능은?
H, M = time(HV, MV)
print(H,M)
