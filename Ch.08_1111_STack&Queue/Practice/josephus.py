def enqueue(queue, element):
    queue.append(element)
    
def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def empty(queue):
    return len(queue) == 0

def josephus(n,k):
    queue, sequence = [], []
    for i in range(1, n+1):
        enqueue(queue,i)
    j = 1
    #계속 삭제니까 empty 안될때까지 계속 돌림
    while not empty(queue):
        cur = dequeue(queue)
        if j % k == 0:
            enqueue(sequence, cur)
        else:
            enqueue(queue,cur)
        j += 1
    return sequence 

print(josephus(7,3))
print(josephus(41,3))