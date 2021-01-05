class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#%%基本操作

queue_1 = Queue()

for i in range(6):
    queue_1.enqueue(i)

queue_1.dequeue()
print(queue_1.items)
print(queue_1.size())
