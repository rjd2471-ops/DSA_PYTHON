#Ques find the pair of the given sum in DoublyLinkedList
#The linked list is in sorted manner and no element is repeated in this  is.


class Node:
    def __init__(self,val):
        self.val= val
        self.next= None
        self.prev= None
        
n1= Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)
n5= Node(50)
         
n1.next= n2
n2.prev= n1
n2.next= n3
n3.prev= n2
n3.next= n4
n4.prev= n3
n4.next= n5
n5.prev= n4

head= n1
temp= head
while temp.next:
    temp= temp.next
tail= temp

target=70
result=[]
while head != tail and tail.next != head:
    total= head.val+ tail.val
    if total == target:
        result.append([head.val,tail.val])
        head= head.next
        tail= tail.prev
    elif total< target:
        head= head.next
    else:
        tail= tail.prev
print(result)
#This is the most optimal sol for this is and its time comp is O(N) and space comp is O(1).