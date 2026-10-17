#Ques Find the maximum sum in the binary tree.

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

maxi=0
def solve(node):
    
    if node is None:
        return 0
    
    global maxi
    
    left_sum=solve(node.left)
    
    if left_sum<0:
        left_sum=0
        
    right_sum= solve(node.right)
    
    if right_sum<0:
        right_sum=0
        
    maxi= max(maxi, left_sum+ node.val+right_sum)
    
    return node.val+ max(left_sum, right_sum)

solve(root)

print(maxi)
#Here time comp is O(N) and space comp is O(height).