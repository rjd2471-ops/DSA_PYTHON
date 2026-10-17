#Question Reverse a Doubly linked list.
class Node:
    def __init__(self,val):
        self.val= val
        self.next= None
        self.prev= None
        
n1= Node(10)
n2= Node(20)
n3= Node(30)
n4= Node(40)
n1.next= n2
n2.prev= n1
n2.next= n3
n3.prev= n2
n3.next= n4
n4.prev= n3
head= n1

first= None
second= head
while second:
    if first is None:
        temp= second.next
        second.next = first
        first= second
        second= temp
    else:
     temp= second.next
     second.next = first
     first.prev= second
     first= second
     second= temp

head= first

print(head.val)
print(head.next.val)
print(head.next.prev.val)
print(head.next.next.prev.val)
print(head.next.next.val)
#Here the time comp is O(N) and space comp is O(1).