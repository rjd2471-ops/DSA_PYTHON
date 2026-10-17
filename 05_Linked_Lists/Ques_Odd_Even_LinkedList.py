#Question Write Odd nodes first then even node in a linked list.
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


#Lets try the brute force approch for this is.


if head is None or head.next is None:
    print(head)
    
else:
    result=[]
    temp=head
    
    while temp :
        result.append(temp.val)
        
        if temp.next:
            temp = temp.next.next
        else:
            break
        
    temp= head.next
    
    while temp :
        result.append(temp.val)
        if temp.next:
            temp = temp.next.next
        else:
            break
        
    temp=head
    index=0
    
    while temp is not None :
        temp.val= result[index]
        index+=1
        temp=temp.next
    print(head.next.val)
    
#Here the time comp is O(N) and space comp is O(N).


#Lets try the Optimal sol for this is.

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

if head is None or head.next is None:
    print(head)
    
else:
 odd= head
 even= head.next
 even_head= head.next


 while even and even.next :
    odd.next= odd.next.next
    odd= odd.next
    
    even.next= even.next.next
    even= even.next
    
 odd.next= even_head
    
#Here the time comp is O(N) and space comp is O(1).