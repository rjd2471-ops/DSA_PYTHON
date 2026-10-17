#Question is that reverse a linked list.
class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(50)

head= node1
node1.next=node2
node2.next= node3
node3.next= node4
node4.next= node5

curr= head
prev= None
while curr is not None:
    next_node= curr.next
    curr.next=prev
    prev= curr
    curr=next_node
    
    
head = prev
print(head.val)