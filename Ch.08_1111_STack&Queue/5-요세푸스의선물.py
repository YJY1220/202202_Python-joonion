def enqueue(queue,element):
    queue.append(element)

def dequeue(queue):
    if len(queue) == 0:
        return None
    return queue.pop(0)

def empty(queue):
    return len(queue) == 0

def josephus(n):
    circle, sequence = [i for i in range(1,n+1)], []
    j = 0
    t = 1
    while len(circle) != 1 :
        j = (j + t**3 - 1) % len(circle) #탈락자 1
        sequence.append(circle.pop(j))
        t += 1
    return circle[0]

N = int(input())
print(josephus(N))