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
Problem 3: Pruning Plans
You have a large overgrown Magnolia tree that's in desperate need of some pruning. Before you can prune the tree, you need to do a full survey of the tree to evaluate which sections need to be pruned.

Given the 'root' of a binary tree representing the magnolia, return a list of the values of each node using a postorder traversal. In a postorder traversal, you explore the left subtree first, then the right subtree, and finally the root. Postorder traversals are often used when deleting nodes from a tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input
    O - Output 
    C - constraints/considerations
        Perform postorder traversal: 
            left, right, root
    E - example/edge cases
        HAPPY CASE
        Input: Binary tree with nodes ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]
        Output: ["Leaf1", "Node1", "Leaf2", "Leaf3", "Node2", "Root"]
        Explanation: The postorder traversal visits the nodes in the correct order.

        EDGE CASE
        Input: Binary tree with only one node
        Output: ["Root"]
        Explanation: The single node is the root and is returned as the only element.  
        - How should the function behave if the tree is empty?
            The function should return an empty list if the tree is empty.
M-atch:
    Binary tree traversal: 
    Recursion: 
P-lan:
    High-level: 
        Traverse the tree using postorder traversal and collect the node values.
    Steps: 
        1. Base case: if not root, return empty list
        2. Recursive case:

        3. Return left + right + root

I-Implement
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    pass

# Example Usage:
"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
"""

magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))

# Example Output: 
# ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']

'''
6: E-valuate
Evaluate the performance of your algorithm and state any strong/weak or future potential work.

Assume N represents the number of nodes in the binary tree.

    - Time Complexity: O(N) because the algorithm visits each node once.
    - Space Complexity: O(H) where H is the height of the tree, due to the recursive call stack.
'''