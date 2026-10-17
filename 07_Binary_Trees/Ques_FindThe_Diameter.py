#Ques find the longest path of a binary tree. Here their is no condition that it would pass through root.

# Ques find the longest path of a Binary Tree.
# The path does NOT necessarily pass through the root.

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

diameter=0

def solve(node):
    
    global diameter
    
    if node is None:
        return 0
    
    lh= solve(node.left)
    
    rh = solve(node.right)
    
    diameter= max(diameter, lh+rh)
    
    return 1+max(lh,rh)

solve(root)

print(diameter)

#Time Complexity  = O(N)
#Space Complexity = O(H)