#Question Delete all the occurance of a val in a Doubly linked list.
class Node:
    def __init__(self,val):
        self.val= val
        self.next= None
        self.prev= None
        
n1= Node(10)
n2= Node(20)
n3= Node(10)
n4= Node(40)
n1.next= n2
n2.prev= n1
n2.next= n3
n3.prev= n2
n3.next= n4
n4.prev= n3
head= n1

value= 10
temp = head

while temp:
    new_node= temp.next
    
    if temp.val== value:
        
        if temp== head:
            head= head.next
            if head:
                head.prev= None
        else:
            temp.prev.next= temp.next
            if temp.next:
                temp.next.prev= temp.prev
                
    temp= new_node