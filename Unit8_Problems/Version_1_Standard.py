
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
print_tree(None)

'''
Problem 1: Grafting Apples
You are grafting different varieties of apple onto the same root tree can produce many different varieties of apples! Given the following TreeNode class, create the binary tree depicted below. The text representing each node should should be used as the value.

The root, or topmost node in the tree TreeNode("Trunk") has been provided for you.
             
P-lan
    Steps: 
        1) Start with the root node "Trunk".
        2) Assign "Mcintosh" as the left child of "Trunk".
        3) Assign "GrannySmith" as the right child of "Trunk".
        4) Assign "Fuji" and "Opal" as the left and right children of "Mcintosh", respectively.
        5) Assign "Crab" and "Gala" as the left and right children of "GrannySmith", respectively.
        6) The binary tree is now constructed as depicted in the problem.    
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk")
# Children
root.left = TreeNode('Mcintosh')
root.right = TreeNode('Granny Smith')
# Grandchildren
root.left.left = TreeNode('Fuji')
root.left.right = TreeNode('Opal')
root.right.left = TreeNode('Crab')
root.right.right = TreeNode('Gala')
# Example Usage:

# Using print_tree() included at the top of this page
# print_tree(root)
'''
Example Output:

['Trunk', 'Mcintosh', 'Granny Smith', 'Fuji', 'Opal', 'Crab', 'Gala']
'''

'''
Problem 2: Calculating Yield
You have a fruit tree represented as a binary tree with exactly three nodes: the root and its two children. Given the root of the tree, evaluate the amount of fruit your tree will yield this year. The tree has the following form:

    Leaf nodes have an integer value.
    The root has a string value of either "+", "-", "*", or "-".
The yield of a the tree is calculated by applying the mathematical operation to the two children.

Return the result of evaluating the root node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity.

    U - Understand
        I - Input - Given the 'root' of the tree, evaluate the amount of fruit your tree will yield this year
        O - Output 
            Return the result of evaluating the root node.
        C - constraints/considerations
            The root has a string value of either "+", "-", "*", or "/".
            What do the leaf nodes represent?
                The leaf nodes represent integer values.
        E - example/edge cases
            HAPPY CASE
            Input: A binary tree with root value of "+" and children 7 and 5
            Output: 12
            Explanation: The "+" operation is applied to the two children: 7 + 5 = 12.

            EDGE CASE
                Input: A binary tree with root value of "-" and children 10 and 20
                Output: -10
                Explanation: The "-" operation is applied to the two children: 10 - 20 = -10.
                - Division by 0
    M-atch 
        Binary Tree traversal 
        Recursion

    P - Plan
        High-level: 
            calculated the yield of a the tree by applying the mathematical operation to its two children.   
        Steps: 
            1) Check the value of the root node.
            2) If the value is "+":
                a) Return the sum of the left and right children.
            3) If the value is "-":
                a) Return the difference between the left and right children.
            4) If the value is "*":
                a) Return the product of the left and right children.
            5) If the value is "/":
                a) Return the quotient of the left and right children.
    I - Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
def calculate_yield(root):
    if root.val == '+':
        return root.left.val + root.right.val
    elif root.val == '-':
        return root.left.val - root.right.val
    elif root.val == '*':
        return root.left.val * root.right.val
    elif root.val == '/':
        if root.right.val != 0:
            return root.left.val // root.right.val
        else: 
            return 'Devision by 0'
    
# Example Usage:
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))
apple_tree_minus = TreeNode("-", TreeNode(10), TreeNode(20))
apple_tree_times = TreeNode("*", TreeNode(7), TreeNode(5))
apple_tree_dev = TreeNode("/", TreeNode(7), TreeNode(0))
apple_tree_dev_by0 = TreeNode("/", TreeNode(7), TreeNode(1))

# print(calculate_yield(apple_tree))
# print(calculate_yield(apple_tree_minus))
# print(calculate_yield(apple_tree_times))
# print(calculate_yield(apple_tree_dev))
# print(calculate_yield(apple_tree_dev_by0))
'''
Example Output:

12
'''
'''    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''