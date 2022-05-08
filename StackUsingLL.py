class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class StackLL:
    def __init__(self):
        self.LinkedList = LinkedList()

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

myStack = StackLL()
print(myStack.isEmpty())