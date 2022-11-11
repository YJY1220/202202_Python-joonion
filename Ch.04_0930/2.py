DIFF = ord('a') - ord('A')

# Let solve() return merged list
def solve(s, t):
    res = s+t
    #무조건 소문자가 앞에 오도록 됨!!! 아스키코드가 소문자가 더 높음
    #ord는 아스키코드화
    res.sort(key = lambda x: (ord(x.upper()), -ord(x)))
    return res

S, T = input().split()
#upper 하나씩 되므로 괜히 깝치지 말자
S = sorted(list(S.upper()))
T = sorted(list(T.lower()))
print(" ".join(solve(S, T)))