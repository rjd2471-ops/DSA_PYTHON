#Question Find the Middle element of a linked list .
class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(50)

head=node1
node1.next=node2
node2.next= node3
node3.next= node4
node4.next= node5

temp= head
n=0

while temp is not None:
    n+=1
    temp=temp.next
    
    
temp= head

for _ in range(n//2):
    temp=temp.next
print(temp.val)

#Lets apply the most optimal sol for this is.

class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(50)

head=node1
node1.next=node2
node2.next= node3
node3.next= node4
node4.next= node5

first=head
second= head
while second is not None and second.next is not None:
    first=first.next
    second=second.next.next
print(first.val)
#Here the time comp is O(N/2) and space comp is O(1).