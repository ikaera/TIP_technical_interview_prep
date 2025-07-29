# Testing your Binary Tree (Printing)
from collections import deque 

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, TreeNode(5), TreeNode(6)))

# print_tree(root)
# print_tree(None)


'''

U-nderstand:
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/edge cases
M-atch:
P-lan:
    High-level: 

    Steps: 
        1. 
        2. 

I-Implement
'''
