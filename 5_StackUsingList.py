class stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        if self.list == None:
            return "Stack is empty"
        else:
            values = self.list.reverse()
            values = [str(x) for x in self.list]
            return "\n".join(values)

    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self,value):
        self.list.append(value)
        return "element added successfully"

    def pop(self):
        if self.list == []:
            return "Stack is empty"
        else:
            return self.list.pop()
    
    def peek(self):
        if self.list == []:
            return "Stack is empty"
        else:
            return self.list[-1]

    def delete(self):
        self.list = None
        return "Stack is deleted"


    
customStack = stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.push(4)

# customStack.pop()
# print(customStack.peek())

customStack.delete()

print(customStack)