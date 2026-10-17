#Stack and Queues.
#Important topic
#Stack and queues
#Implement stack using array\list.
#What is stack=> we can store any type of data(float,int,str,objects).
#What mechanisum is used-> LIFO[last in first out].
#Because in this we can take out data from one end of the stack so here happens last in first out.


class Stack:
    def __init__(self):
        self.items=[]
        
    def is_empty(self):
        return len(self.items)==0
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        if len(self.items)==0:
            return "Can not pop, stack is empty"
        x=self.items.pop()
        return x
    
    
    def top(self):
        if len(self.items)==0:
            return "Can not top, stack is empty"
        return self.items[-1]
    def size(self):
        
        return len(self.items)
    
    
stack=Stack()
stack.push(5)
stack.push(10)
stack.push(15)


print(f"stack contant ={stack}")
print(f"popped item ={stack.pop()}")
print(f"stack conatant ={stack}")
print(f"top item after pop={stack.top()}")
print(f"stack is empty ={stack.is_empty()}")
#Here time comp is O(1).





