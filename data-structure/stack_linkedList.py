class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None


class Stack:
    def __init__(self):
        self.head = None

    def __str__(self):
        printStr = []
        node = self.head

        while(node is not None):
            printStr.append(str(node.data))
            node = node.prev
        return ", ".join(printStr)

    def push(self, data):
        print(f"< push -> {data} >")
        
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.prev = self.head
            self.head = new_node


        print(self)

    def pop(self):
        print("< pop >")
        ret = None
        if self.isEmpty():
            print("stack is None")
        else:
            node = self.head
            ret = node.data
            self.head = self.head.prev
            del node
            print(self)
        
        return ret
    
    def isEmpty(self):
        return self.head is None 


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

# < isEmpty ? [True] >
# < push -> 1 >
# 1
# < push -> 2 >
# 2, 1
# < push -> 3 >
# 3, 2, 1
# < pop >
# 2, 1
# < isEmpty ? [False] >
# < push -> 4 >
# 4, 2, 1
# < pop >
# 2, 1
# < push -> 5 >
# 5, 2, 1
# < pop >
# 2, 1
# < pop >
# 1
# < pop >
# 
# < pop >
# stack is None
# < isEmpty ? [True] >