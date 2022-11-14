def solve(num):
    card = list(range(1,num+1))
    while(1):
        if len(card) == 1:
            break
        card.pop(0)
        card.append(card.pop(0))
            
    return card[0]
    

N = int(input())
print(solve(N))