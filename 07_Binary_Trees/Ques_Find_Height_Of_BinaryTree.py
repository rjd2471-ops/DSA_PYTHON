#Ques find the height of a Binary Tree.

class Node:
    
    def __init__(self,val):
        self.val= val
        self.left=None
        self.right=None
        
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

n3.right = n6

n4.left = n7

n5.right = n8

n7.left = n9

n9.right = n10

root = n1

from collections import deque
def bfs(node):
    queue= deque([])
    
    queue.append(node)
    count=0
    while queue:
        h= len(queue)
        for _ in range(h):
            e=queue.popleft()
        
            if e.left:
               queue.append(e.left)
            
            if e.right:
               queue.append(e.right)
        count+=1
            
    return count
print(bfs(root))
#here this is the optimal sol for this is the time comp for this is O(N) and space comp is O(weidth~=N/2=N).