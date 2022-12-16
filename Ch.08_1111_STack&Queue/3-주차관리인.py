def push(stack, element):
    stack.append(element)

def pop(stack):
    if(isEmpty(stack)):
        return None
    A =stack.pop()
    return A

def isEmpty(stack):
    return len(stack) == 0

def solve(S,N):
  index = 0
  AR = list(range(1,N+1))
  stack = []
  ANS = []
  for i in range(N):
    if S[index] == AR[i]:
      push(ANS, AR[i])
      index += 1
      while (not isEmpty(stack)) and stack[-1] == S[index]:
        push(ANS, pop(stack))
        index += 1
    else:
      push(stack,AR[i])
          
  for i in range(len(stack)):
    push(ANS, pop(stack))
        
  if ANS == S:
    return "yes"
  else:
    return "no"
    


N, T = map(int, input().split())
ANS = []

for i in range(T):
    sol = list(map(int, input().split(',')))
    ANS.append(solve(sol,N))

for i in range(T):
    print(ANS[i])