class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None

class SinglyLLNode:
    def __init__(self, value = Null):
        self.value = value
        self.next = Null

SingLL = SinglyLL()

node1 = SinglyLLNode(1)
node2 = SinglyLLNode(2)

SinglyLL.head = node1
SinglyLL.head.next = node2
SinglyLL.tail = node2

