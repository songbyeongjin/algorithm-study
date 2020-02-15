class Stack:
    def __init__(self):
        self.builtInstack = []


stack = Stack()
stack.builtInstack.insert(0, 1)
stack.builtInstack.insert(0, 2)                
stack.builtInstack.insert(0, 3)
stack.builtInstack.pop()
stack.builtInstack.insert(0, 4)
stack.builtInstack.pop()
stack.builtInstack.insert(0, 5)
stack.builtInstack.pop()
stack.builtInstack.pop()
stack.builtInstack.pop()
stack.builtInstack.pop()

#IndexError occured at 17 line