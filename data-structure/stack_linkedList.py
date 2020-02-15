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
        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.head
            self.head = new_node
        print(self)

    def pop(self):
        print("< pop >")
        
        if(self.head is not None):
            value = self.head.data
            node = self.head
            self.head = self.head.prev
            del node
            print(self)
        else:
            print("stack is None")
    
    def isEmpty(self):
        isempty = self.head is None
        print(f"< isEmpty ? [{isempty}] >")
        return isempty 


if __name__=="__main__":
    m_stack = Stack()
    m_stack.isEmpty()
    m_stack.push(1)
    m_stack.push(2)
    m_stack.push(3)
    m_stack.pop()
    m_stack.isEmpty()
    m_stack.push(4)
    m_stack.pop()
    m_stack.push(5)
    m_stack.pop()
    m_stack.pop()
    m_stack.pop()
    m_stack.pop()
    m_stack.isEmpty()