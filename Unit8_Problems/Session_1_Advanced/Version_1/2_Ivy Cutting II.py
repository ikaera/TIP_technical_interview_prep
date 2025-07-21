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
Problem 2: Ivy Cutting II
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

If you implemented 'right_vine()' iteratively in the previous problem, implement it recursively. If you implemented it recursively, implement it iteratively.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/
        HAPPY CASE
        Input: Binary tree where the rightmost path is ["Root", "Node2", "Leaf3"]
        Output: ["Root", "Node2", "Leaf3"]
        Explanation: The rightmost path is extracted correctly using recursion.

        EDGE CASE
        Input: Binary tree with no right child at any node
        Output: ["Root"]
        Explanation: The rightmost path consists only of the root node.
        
M-atch:
P-lan:
    High-level: Traverse the tree recursively starting from the root and collect the values of nodes in the rightmost path.

    Steps: 
        1. If the current node is None, return an empty list.
        2. Recursive case: 
        Return a list containing the current node’s value + the result of recursively calling the function on the right child (right_vine(root.right)).        
I-Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def right_vine(root):
  # Base case:
    
  # Recursive case:

  pass

# Example Usage:

"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""
ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

"""
      Root
      /  
    Node1
    /
  Leaf1  
"""
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))
'''
Example Output:

['Root', 'Node2', 'Leaf3']
['Root']'''

'''
6: E-valuate
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

Assume H represents the height of the binary tree.

    - Time Complexity: O(H) because the algorithm traverses down the height of the tree.
    - Space Complexity: O(H) because the recursion stack will use space proportional to the height of the tree.
'''