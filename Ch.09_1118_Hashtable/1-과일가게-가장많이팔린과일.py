N = int(input())
fruit = {}
for i in range(N):
    name = input().strip()
    if (name in fruit.keys()):
        fruit[name] += 1
    else:
        fruit[name] = 1

store = []
store = sorted(fruit.items(),key = lambda x : ( x[0], -x[1]))

for i in range(len(store)):
    print(" ".join(map(str,store[i])))
