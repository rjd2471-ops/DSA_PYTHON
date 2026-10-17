#Ques Find the right side view of a Binary tree.

class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n4.left = n6
n6.left = n7

n3.right = n8
n8.right = n9
n9.right = n10

root = n1

from collections import deque

def rightsideView(node):
    
    if node is None:
        return
    queue= deque([])
    
    result=[]
    
    queue.append(node)
    
    while queue:
        l= len(queue)
        
        for i in range(l):
            e= queue.popleft()
            
            if i == l - 1:
                result.append(e.val)
                
            if e.left:
                queue.append(e.left)
                
            if e.right:
                queue.append(e.right)
        
    return result

print(rightsideView(root))
            
#for this  the time comp for this is O(N) and space comp is O(weidth~=N/2=N).



class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n4.left = n6
n6.left = n7

n3.right = n8
n8.right = n9
n9.right = n10

root = n1

def rightsideView(node=root, level=0, result=[]):
    
    if node is None:
        return
    
    if level== len(result):#"Have I reached this depth for the first time."
        result.append(node.val)
        
    rightsideView(node.right,level+1,result)
    
    rightsideView(node.left, level+1,result)
    
    return result
    
print(rightsideView())
#This is the most optimal sol here time comp is O(N) and space comp is O(Height).