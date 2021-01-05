class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

#%%基本操作

stack = Stack()
stack.push(1)
stack.pop()

for i in range(6):
    stack.push(i)

print(stack.items)
print(stack.peek())
print(stack.size())

#%%要素の順番の逆転

stack_1 = Stack()
for k in 'Hello':
    stack_1.push(k)

reverse = ''
while stack_1.size():
    reverse += stack_1.pop()

print(reverse)
