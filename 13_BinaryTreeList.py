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

    
newBT = BinaryTree(8)
newBT.insertNode('Drinks')
newBT.insertNode('Hot')
newBT.insertNode('Cold')
print(newBT.List)
