class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

class StackLL:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self,value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        val = self.LinkedList.head.value
        nextNode = self.LinkedList.head.next
        return val

    def peek(self):
        if self.isEmpty():
            return "Empty Stack"
        else:
            val = self.LinkedList.head.value
            return val

    def delete(self):
        self.LinkedList.head = None


myStack = StackLL()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
print(myStack.isEmpty())
print(myStack)
print("---------------")
# print(myStack.pop())
print(myStack.peek())
print("---------------")

