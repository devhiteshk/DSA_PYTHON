class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def createDLL(self, value):
        newNode = Node(value)
        newNode.next = None
        newNode.prev = None
        self.head = newNode
        self.tail = newNode
        return "DLL created successfully"

DLL = DoublyLL()
DLL.createDLL(5)
print([node.value for node in DLL])