def solve(s):
    bracket = []
    cnt = 0
    for i in range(len(s)):
        if s[i] == "(":
            bracket.append(s[i])
        else:
            if len(bracket) == 0:
                cnt+=1
                continue
            bracket.pop()
    return cnt+len(bracket)

S = input()
print(solve(S))
    