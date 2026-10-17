#Ques Find the top view of a binary tree.

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

def topview(node):
    if node is None:
        return None
    
    ans=[]
    
    q=deque([])
    
    result={}
    
    q.append((node,0))
    
    while q:
        e,line=q.popleft()
        
        if line not in result:
            result[line]=e.val
            
        if e.left is not None:
            q.append((e.left,line-1))
            
        if e.right is not None:
            q.append((e.right,line+1))
            
    for value in sorted(result.items()):
        ans.append(value[1])
        
    return ans

print(topview(root))

#So here its time commp is O(Nlog(N)) and space comp is O(N).
