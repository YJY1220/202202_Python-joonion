def enqueue(queue, element):
    queue.append(element)
    
def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def empty(queue):
    return len(queue) == 0

def josephus(n,k):
    circle, sequence = [i for i in range(1,n+1)], []
    j = 0
    while len(circle) > 0:
        j = (j+k-1) % len(circle)
        sequence.append(circle.pop(j))
    return sequence 

print(josephus(7,3))
print(josephus(41,3))