#Question implimantation of queues [] stack.
#This is a kind of ticket counter in which people csn form line and the person who goes first in line
#go first out of the line.
class Queue:
    def __init__(self):
        self.items=[]
        
        
    def is_empty(self):
        return len(self.items)==0
    
    
    def enqueue(self,item):
        self.items.append(item)
        
        
    def dequeue(self):#this is an O(n) operation.
        if len(self.items)==0:
            return "Can not pop, stack is empty"
        
        x=self.items.pop(0)
        return x
    
    
    def front(self):
        if len(self.items)==0:
            return "queue is empty"
        return self.items[0]
    
    
    def rear(self):
        if len(self.items)==0:
            return "queue is empty"
        return self.items[-1]
    
    
    def size(self):
        return len(self.items)
    
    
    
    
#Here time comp is O(n).

