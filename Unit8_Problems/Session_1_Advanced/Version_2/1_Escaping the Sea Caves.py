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
Problem 1: Escaping the Sea Caves
You are given the root of a binary tree representing possible route through a system of sea caves. You recall that so long as you take the leftmost branch at every fork in the route, you'll find your way back home. Write a function leftmost_path() that returns an array with the value of each node in the leftmost path.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input - the root of a binary tree
    O - Output - array or list with the value of each node in the leftmost path.
    C - constraints/ leftmost path
            considerations 
            Assume the input tree is balanced when calculating time and space complexity
    E - example/edge cases
        HAPPY CASE
        Input: Binary tree with nodes ["CaveA", "CaveB", "CaveD", "CaveE", "CaveC", "CaveF"]
        Output: ["CaveA", "CaveB", "CaveD"]
        Explanation: The leftmost path is ["CaveA", "CaveB", "CaveD"].

        EDGE CASE
        - root has on left child, return root arra wiht only the root value
        - Input: Binary tree with nodes ["CaveA", "CaveB", "CaveC"] where the root has only right children.
        Output: ["CaveA"]
        Explanation: The root has no left children, so the path only includes the root.
M-atch: Binary trere traversal
    Iteration
P-lan:
    High-level: 

    Steps: 
        1. Init "result" an empty array
        2. cur = root
        3. while loop (curr is not None):
            1. append the current node's value to the result array
            2. Move toward left of the current node
        4. return result

I-Implement
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def leftmost_path(root):
    result = []
    cur = root
    while cur:
        result.append(cur.val)
        cur = cur.left
    
    return result

# Example Usage:

"""
          
"""
system_a = TreeNode("CaveA", 
                  TreeNode("CaveB", TreeNode("CaveD"), TreeNode("CaveE")), 
                          TreeNode("CaveC", None, TreeNode("CaveF")))

"""
  
"""
system_b = TreeNode("CaveA", None, TreeNode("CaveB", None, TreeNode("CaveC")))

print(leftmost_path(system_a))
print(leftmost_path(system_b))
'''Example Output:

['CaveA', 'CaveB', 'CaveD']
['CaveA']
'''
