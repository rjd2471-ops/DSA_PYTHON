#Ques Remove Duplicates from a sorted Doubly linked list.
class Node:
    def __init__(self,val):
        self.val= val
        self.next= None
        self.prev= None
        
n1= Node(10)
n2= Node(10)
n3= Node(10)
n4= Node(10)
n5= Node(10)
         
n1.next= n2
n2.prev= n1
n2.next= n3
n3.prev= n2
n3.next= n4
n4.prev= n3
n4.next= n5
n5.prev= n4

head= n1
temp1= head
temp2= head.next
while temp1 and temp2 :
    while temp2 and temp1.val== temp2.val :
        temp2= temp2.next
    if temp2:
        next_node= temp2.next
        temp2.prev= temp1
        temp1.next= temp2
        
        temp1= temp2
        temp2= next_node
    else:
        temp1.next= None
print(head.val)
#print(head.next.val)
#print(head.next.next.next.val)
