# whith no size capacity

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        values = [str(x) for x in self.items]
        return '-'.join(values)

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self,value):
        self.items.append(value)
        return "Item added successfully"

    def dequeue(self):
        if self.isEmpty():
            return "Empty"
        else:
            self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.items[0]
        
    def delete(self):
        self.items = None

myQueue = Queue()
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)

myQueue.dequeue()
print(myQueue.peek())
myQueue.delete()
print(myQueue)
