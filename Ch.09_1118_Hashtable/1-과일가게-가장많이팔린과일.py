N = int(input())
fruit = {}
for i in range(N):
    name = input().strip()
    if (name in fruit.keys()):
        fruit[name] += 1
    else:
        fruit[name] = 1

store = []
store = sorted(fruit.items(),key = lambda x : (-x[1], x[0]))

print(store[0][0])
print(store[0][1])