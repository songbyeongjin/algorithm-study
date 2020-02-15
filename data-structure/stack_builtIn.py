class Stack:
    def __init__(self):
        self.builtInstack = []


stack = Stack()
stack.builtInstack.append(1)
stack.builtInstack.append(2)                
stack.builtInstack.append(3)
stack.builtInstack.pop()
stack.builtInstack.append(4)
stack.builtInstack.pop()
stack.builtInstack.append(5)
stack.builtInstack.pop()
stack.builtInstack.pop()
stack.builtInstack.pop()
stack.builtInstack.pop()

#IndexError occured at 17 line