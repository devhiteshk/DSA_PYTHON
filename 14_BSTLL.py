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



class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
        return
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)
    return "Node added to BST"

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not (myQueue.isEmpty()):
            root = myQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)

newBST = BSTNode(None) 
insertNode(newBST, 70)
insertNode(newBST, 60)
print(newBST.data)   
print(newBST.leftChild.data)   