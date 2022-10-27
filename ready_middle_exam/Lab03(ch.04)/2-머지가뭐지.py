DIFF = ord('a') - ord('A')

def solve(s,t):
    res = s+t 
    res.sort(key = lambda x : (ord(x.upper()), -ord(x)))
    return res 
S,T = input().split()
S = sorted(list(S.upper()))
T = sorted(list(T.lower()))
print(" ". join(solve(S,T)))