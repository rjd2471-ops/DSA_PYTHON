#Doubly linked list.

class Node:
    def __init__(self,val):
        self.val= val
        self.next= None
        self.prev= None
        
n1= Node(10)
n2= Node(20)
n3= Node(30)

n1.next= n2
n2.prev= n1
n2.next= n3
n3.prev= n2


class DoublyLinkedList:
    def __init__(self):
        self.head= None
#insert at head
    def insert_at_head(self,val):
        new_node= Node(val)
        if not self.head:
            self.head= new_node
        else:
            new_node.next= self.head
            self.head.prev= new_node
            self.head= new_node
            
    def append(self,val):
        new_node= Node(val)
        if not self.head:
            self.head= new_node
        else:
            curr= self.head
            while curr:
                curr= curr.next
            curr.next= new_node
            new_node.prev= curr
            
    def insert_at(self,val,position):
        new_node= Node(val)
        if position== 0:
            new_node.next = self.head

            if self.head:
               self.head.prev = new_node

            self.head = new_node
            return

            
        curr= self.head
        count=0
        while curr and count< position-1:
            count+=1
            curr= curr.next
        if curr is None:
            print("Index out of bound")
            return
        new_node.next= curr.next
        new_node.prev= curr
        if curr.next:
           curr.next.prev= new_node
        curr.next= new_node
            
            
        