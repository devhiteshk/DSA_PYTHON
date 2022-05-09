class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class Queue:
    def __init__(self):
        self.LL = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.LL]
        return ' '.join(values)

    def enqueue(self,value):
        newNode = Node(value)
        if self.LL.head is None:
            self.LL.head = newNode
            self.LL.tail = newNode

        else:
            self.LL.tail.next = newNode
            self.LL.tail = newNode

    def isEmpty(self):
        if self.LL.head == None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            temp = self.LL.head
            if self.LL.head == self.LL.tail:
                self.LL.head = None
                self.LL.tail = None
            else:
                self.LL.head = self.LL.head.next
            return temp

    def peek(self):
        if self.isEmpty():
            return "Empty Queue"
        else:
            return self.LL.head

    def delete(self):
        self.LL.head = None
        self.LL.tail= None

myQueue = Queue()
myQueue.enqueue(5)
myQueue.enqueue(3)
myQueue.enqueue(1)
myQueue.enqueue(4)
print(myQueue)
myQueue.dequeue()
print(myQueue)
print(myQueue.peek())