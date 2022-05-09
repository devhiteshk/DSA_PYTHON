class BinaryTree:
    def __init__(self,size = None):
        self.List = size*[None]
        self.lastUsedIndex = 0
        self.MaxSize = size

    # def __iter__(self):
    #     values = [str(i) for i in self.List]
    #     return values

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.MaxSize:
            return "BT is full"
        self.List[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "value added"

    def searchNode(self, nodeValue):
        for i in range(len(self.List)):
            if self.List[i] == nodeValue:
                return "success"
        return "Not Found"

    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.List[index])
        self.preOrderTraversal(index*2)
        self.preOrderTraversal(index*2 + 1)
                
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2)
        print(self.List[index])
        self.inOrderTraversal(index*2 + 1)

    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 + 1)
        print(self.List[index])

    def levelorderTraversal(self,index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.List[i])

    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            return "No node to delete"

        for i in range(1,self.lastUsedIndex + 1):
            if self.List[i] == value:
                self.List[i] = self.List[self.lastUsedIndex]
                self.List[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "Node Deleted"

    def deleteBT(self):
        self.List = None
        return "Binary Tree Deleted"

newBT = BinaryTree(8)
newBT.insertNode('Drinks')
newBT.insertNode('Hot')
newBT.insertNode('Cold')
print(newBT.List)

# newBT.preOrderTraversal(1)
# newBT.inOrderTraversal(1)
# newBT.postOrderTraversal(1)
newBT.deleteNode('Hot')
newBT.levelorderTraversal(1)
