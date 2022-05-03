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
            
    def TraverseSLL(self):
        if self.head is None:
            print("SLL donesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next 

    def SearchSLL(self, value):
        if self.head is None:
            return "SLL is empty"
        else:
            pos = 0
            node = self.head
            while node is not None:
                if node.value == value:
                    return "Found element at: ", pos
                pos += 1
                node = node.next
            return "element dont exist"

    def deleteNode(self, location):
        if self.head is None:
            print("SLL is empty")

        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                
            if location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            else:
                tempNode = self.head
                index = 0
                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                
    def deleteEntireLL(self):
        self.head = None
        self.tail = None

SingLL = SinglyLL()

SingLL.insertSLL(1,1)
SingLL.insertSLL(2,1)
SingLL.insertSLL(3,1)
SingLL.insertSLL(4,1)

SingLL.insertSLL(10,0)

SingLL.insertSLL(3,3)

# SingLL.TraverseSLL()
print([node.value for node in SingLL])
SingLL.deleteNode(3)
SinglyLL.deleteEntireLL()
print([node.value for node in SingLL])

# print(SingLL.SearchSLL(100))

