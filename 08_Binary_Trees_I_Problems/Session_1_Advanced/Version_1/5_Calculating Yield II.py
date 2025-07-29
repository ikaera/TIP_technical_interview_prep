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
Problem 5: Calculating Yield II
You have a fruit tree represented as a binary tree. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

Leaf nodes have an integer value.
Non-leaf nodes have a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated as follows:

If the node is a leaf node, the yield is the value of the node.
Otherwise evaluate the node's two children and apply the mathematical operation of its value with the children's evaluations.
Return the result of evaluating the root node.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input
    O - Output 
        What does the function need to return?
            The function needs to return the result of evaluating the arithmetic expression represented by the tree.
    C - constraints/considerations
        What does each node in the binary tree represent?
            Leaf nodes represent numeric values, and non-leaf nodes represent arithmetic operators.

        
    E - example/edge cases
        
        EDGE CASE
        Input: 
        Tree structure with only one node:
            5
        Output: 5
        How should the function behave if the tree is empty?
            The problem does not specify an empty tree case, but in general, an empty tree might return 0 or an error depending on the context.
Explanation: The tree has only one node, so the result is 5.
M-atch:
P-lan:
    High-level: 
        Traverse the tree recursively, calculating the result of the expression by applying operations at each non-leaf node.
    Steps: 
        1. 
        2. 

I-Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
  pass

# Example Usage:

"""      
"""

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))
'''
Example Output:

22
Explanation:
- 4 - 2 = 2
- 10 * 2 = 20
- 2 + 20 = 22'''