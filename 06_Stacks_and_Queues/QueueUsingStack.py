#Topic implimenting the queue using the stack.


class QueueUsingStack:
    def __init__(self):
        self.st1 = []
        self.st2 = []
        
    def push(self,val):
        if not self.st1:
            self.st1.append(val)
            
        else:
            while self.st1:
                self.st2.append(st1.pop())
            self.st1.append(val)
            while self.st2:
                self.st1.append(st2.pop())
        
            