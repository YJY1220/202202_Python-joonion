def enqueue(queue, element):
    queue.append(element)
    
def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def empty(queue):
    return len(queue) == 0

def josephus(n,k):
    if n==1:
        return 1
    else:
        return ((josephus(n-1,k) + k - 1) % n) + 1
print(josephus(7,3))
print(josephus(41,3))