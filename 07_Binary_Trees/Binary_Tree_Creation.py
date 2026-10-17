#Topic Binary Tree.

class Node:
    def __init__(self,val):
        self.val= val
        self.left= None
        self.right= None

n1=Node(100)
n2=Node(50)
n3=Node(10)
n4=Node(20)
n5=Node(30)

n1.left=n2
n1.right=n3
n2.left=n4
n3.right= n5
