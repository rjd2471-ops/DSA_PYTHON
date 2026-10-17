#Ques Find the minimum in a stack using O(1) operation.

class Stack:
    def __init__(self):
        self.item= []
        self.min_num= float("inf")
        self.min_item= []
        
    def push(self,data):
        if data<= self.min_num:
            self.min_num= data
            self.min_item.append(self.min_num)
        self.item.append(data)
        
    def pop(self):
        if not self.item:
            return("No element present")
        value= self.item.pop()
        
        if value== self.min_num:
            self.min_item.pop()
            
            if self.min_item:
                self.min_num= self.min_item[-1]
            else:
                self.min_num = float("inf")
                
        return value
    
    def get_min(self):
        if not self.item:
           return "Stack Empty"
        return self.min_num
    
s=Stack()
s.push(100)
s.push(5)
s.push(2)
s.push(2)    
print(s.item)
s.pop()
s.pop()
print(s.get_min())

    
        
            