N = int(input())
english_store = {}
for i in range(N):
    english = input().strip()
    space = "".join(map(str,sorted(english)))
    
    if(space in english_store.keys()):
        english_store[space] += [english]
    else:
        english_store[space] = [english]
        
for i in english_store.keys():
    english_store[i].sort()

english_store = sorted(english_store.items(), key = lambda x: x[1][0])

for i in range(len(english_store)):
    print(" ".join(map(str,english_store[i][1])))