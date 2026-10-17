class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None

node1= Node(10)
node2= Node(20)
node3= Node(30)
node4= Node(40)
node5= Node(50)

node1.next=node2
node2.next= node3
node3.next= node4
node4.next= node5

print(node1.next.val)


class Node:
    def __init__(self,val):
        self.val= val 
        self.next = None
    
class SinglyLinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,val):
        new_node= Node(val)
        if self.head is None:# if list is empty
            self.head= new_node
            
        else:
            curr=self.head
            while curr.next is not None:#if list is not empty
                curr=curr.next
            curr.next= new_node
    
    def traversal(self):
        if self.head is None:
            print("List is empty")
        else:
            curr= self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr= curr.next
                
    def insert_at(self,val, position):
        new_node= Node(val)
        if position== 0:
            self.head.next= new_node
            self.head= new_node
        else:
            curr= self.head
            prev_node= None
            count=0
            
            while curr is not None and count< position:
                prev_node= curr
                curr= curr.next
                count+=1
            prev_node.next= new_node
            new_node.next= curr
            
    def delete(self,val):
        if position==0:
            self.head=None
        else:
            curr= self.head
            prev_node= None
            
            while curr is not None :
                
                prev_node= curr
                curr= curr.next
                if curr.val== val:
                    return
                
            prev_node.next= curr.next
            