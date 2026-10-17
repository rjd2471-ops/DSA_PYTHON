#Implement Queue by using a stack.

class StackQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]
        
        
    def push(self,item):
        while self.st1:#Here time comp is O(n).
            self.st2.append(self.st1.pop())#Transfer all the element from stack1 to stack2 then add element
                               #in stack one then again transfer element of stack2 to stack1.
        self.st1.append(item)
        while self.st2:
            self.st1.append(self.st2.pop())
            
            
    def pop(self):
        if not self.st1 :
            return "This is empty"
        
        top_element=self.st1.pop()
        return top_element
    
    
    def peek(self):
        if not self.st1 :
            return "This is empty"
        return self.st1[-1]
    
    
    def is_empty(self):
        return not self.st1
    
    
"""Stack
Works on LIFO (Last In First Out)

Queue
Works on FIFO (First In First Out)
    """
