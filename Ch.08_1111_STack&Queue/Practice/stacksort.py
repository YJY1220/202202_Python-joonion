def push(stack, element):
    stack.append(element)

def pop(stack):
    if len(stack) == 0:
        return None
    return stack.pop()

parking = [2,3,1,4,5]
stack = []
push(stack, parking.pop())
push(stack, parking.pop())
push(stack, parking.pop())
print(pop(stack), end = " ")
push(stack, parking.pop())
push(stack, parking.pop())
print(pop(stack), end = " ")
print(pop(stack), end = " ")
print(pop(stack), end = " ")
print(pop(stack), end = " ")

