#Question Remove the Nth node from the last in a linked list.

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
        
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.next= node2
node2.next= node3
node3.next= node4
node4.next= node5
node5.next= node6
head= node1


n=2
temp= head
count=0
while temp:
    count+=1
    temp= temp.next

if n==1 :#It means last Node.
    temp= head
    ind=0
    while temp and ind<count-1-1:
       ind+=1
       temp= temp.next
    temp.next= None
    
elif n== count:
    head= node1.next

else:
    temp= head
    ind=0
    while temp and ind<count-n-1:
       ind+=1
       temp= temp.next
    temp.next= temp.next.next
#This is brute froce soln.



#For optimal soln.
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
        
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)

node1.next= node2
node2.next= node3
node3.next= node4
node4.next= node5
node5.next= node6
head= node1

n=2
slow=fast=head
for _ in range(n):
    fast= fast.next
if fast is None:
    head= head.next
else:   
 while fast.next:
    slow= slow.next
    fast=fast.next
 slow.next= slow.next.next

