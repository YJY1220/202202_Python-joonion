def solve(x):
    if x % 4 == 0 and x % 100 != 0:
        return True
    elif x % 400 == 0:
        return True
    else:
        return False
    
Value = int(input())
if(solve(Value)):
    print(True)
else:
    print(False)