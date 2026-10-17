#Question Find the length of the loop which  is involved in the linked list.
class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(50)

node1.next= node2
node2.next= node3
node3.next= node4
node4.next= node5
node5.next= node2
head= node1


first=head
second= head

while second is not None and second.next  is not None:
    first= first.next
    second= second.next.next
    if first== second:#This means loop is involved in this is.
        count=1
        first=first.next
        while first!= second:
            first=first.next
            count+=1
        
        print(count)
        break
else:
    print("No cycle involved in this is.")

#Here time comp is O(N) and space comp is O(1).