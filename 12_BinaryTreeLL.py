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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    preOrderTraversal(rootNode.rightChild)

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
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)

def searchBT(rootNode, nodeValue):
    if not rootNode:
        return
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            if root.value.data == nodeValue:
                return "Success"
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)
        return "not found"
 

def insertNodeBT(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "successfully inserted"
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "successfully inserted"


def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            if root.value == dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    myQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    myQueue.enqueue(root.value.leftChild)

def deleteNodeBT(rootNode, node):
    if not rootNode:
        return
    else:
        myQueue = Queue()
        myQueue.enqueue(rootNode)
        while not(myQueue.isEmpty()):
            root = myQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "Node deleted successfully"
            if root.value.leftChild is not None:
                myQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                myQueue.enqueue(root.value.rightChild)
        return "Failed to delete"


def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "complete BT deleted"


newBT = TreeNode("Drinks")
leftC = TreeNode("Hot")
rightC = TreeNode("Cold")
lleftC = TreeNode("Coffee")
lrightC = TreeNode("Tea")
newBT.leftChild = leftC
newBT.rightChild = rightC
leftC.leftChild = lleftC
leftC.rightChild = lrightC

levelOrderTraversal(newBT)

deleteNodeBT(newBT, "Tea")

levelOrderTraversal(newBT)
# print(searchBT(newBT,"Ta"))
# print(getDeepestNode(newBT))