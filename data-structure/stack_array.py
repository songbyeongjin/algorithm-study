class Stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def __str__(self):
        return ",".join(self.stack)

    def push(self, data):
        print(f"< push -> {data} >")

        self.stack.insert(len(self.stack), str(data))
        self.top = self.top + 1
        print(self)

    def pop(self):
        print("< pop >")

        ret = None
        if(self.isEmpty()):
            print("stack is None")
        else:
            ret = self.stack[self.top-1]
            del self.stack[self.top-1]
            self.top = self.top - 1

        print(self)
        return ret

    def isEmpty(self):
        return len(self.stack) is 0 

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.push(4)
stack.pop()
stack.push(5)
stack.pop()
stack.pop()
stack.pop()
stack.pop()

# < push -> 1 >
# 1
# < push -> 2 >
# 1,2
# < push -> 3 >
# 1,2,3
# < pop >
# 1,2
# < push -> 4 >
# 1,2,4
# < pop >
# 1,2
# < push -> 5 >
# 1,2,5
# < pop >
# 1,2
# < pop >
# 1
# < pop >
# 
# < pop >
# stack is None