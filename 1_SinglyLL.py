class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None


class SinglyLL:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Insert in Singly LL
    def insertSLL(self,value, location):
        
        if self.head == None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            newNode.next = None

        elif location == 0:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode

        elif location == 1:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = None

        else:
            temp = self.head
            index = 0
            while index<location-1:
                tempNode = temp.next
                index += 1

            nextNode = tempNode.next
            newNode = Node(value)
            tempNode.next = newNode
            newNode.next = nextNode
            if tempNode == self.tail:
                self.tail = newNode
            

SingLL = SinglyLL()

SingLL.insertSLL(1,1)
SingLL.insertSLL(2,1)
SingLL.insertSLL(3,1)
SingLL.insertSLL(4,1)

SingLL.insertSLL(10,0)


SingLL.insertSLL(3,3)

print([node.value for node in SingLL])

