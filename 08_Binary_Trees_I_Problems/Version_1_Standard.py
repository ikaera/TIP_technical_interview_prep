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
''' 
Write a function to determine if a binary tree is balanced. A binary tree is considered balanced if the height difference between the left and right subtrees of every node is at most 1.
Examples:


    U - Understand
        I - Input root 
        O - Output true/false
        C - constraints/considerations

        E - example/edge cases
            Input: root = [3, 9, 20, null, null, 15, 7]
            Output: True
            Input: root = [1, 2, 2, 3, 3, null, null, 4, 4]
Output: False
    P - Plan
        High-level: 

        Steps: 
        1. use func helper(node, height)
        2. base case: At the very bottom of the tree (i.e., node is None), we return True and set the height to 0.
        3. Recurse on left and right subtrees:
            1. Declare two new lists for height: left_height = [0], right_height = [0]
            2. Recursively call the helper on the left and right children
        4. Compute height and check balance at current node
            1. Calculate the current node's height:
                left_height[0] and right_height[0] are the heights of the left and right subtrees.
                    height[0] = max(left_height[0], right_height[0]) + 1
                    why? 
                    -We take the maximum of the two because the height of the current node depends on the tallest subtree.
                    -Then we add 1 to count the edge from the current node down to its child subtree.
            2. Then check if this node is balanced:
           
        Step 5: Combine results
        Step 6: Main Function
            Now call your helper function from the main isBalanced(root):

    I - Implement
'''
def is_balanced(root):

    def helper(node, height):
        # base case:
        if node is None:
            height[0] = 0
            return True
        # recurse on left and rigth subtrees:
        left_height = [0]
        right_height = [0]

        left_balanced=helper(node.left, left_height)
        right_balanced =helper(node.right, right_height)

        height[0] = max(left_height[0], right_height[0]) + 1

        if abs(left_height[0] - right_height[0]) > 1:
            return False
        
        return left_balanced and right_balanced
    return helper(root, [0])


# Helper to build trees manually (for testing)
# Test input 1: root = [3, 9, 20, None, None, 15, 7]
root1 = TreeNode(3,
                 TreeNode(9),
                 TreeNode(20,
                          TreeNode(15),
                          TreeNode(7)))

# print(is_balanced(root1))  # Expected: True

# Test input 2: root = [1, 2, 2, 3, 3, None, None, 4, 4]
root2 = TreeNode(1,
                 TreeNode(2,
                          TreeNode(3,
                                   TreeNode(4),
                                   TreeNode(4)),
                          TreeNode(3)),
                 TreeNode(2))

# print(is_balanced(root2))  # Expected: False

'''  
Write a function to determine if a binary tree is a valid binary search tree (BST). A BST is valid if:
The left subtree of a node contains only nodes with values less than the node’s value.
The right subtree of a node contains only nodes with values greater than the node’s value.
Both left and right subtrees must also be valid BSTs.
Examples:
Input: root = [2, 1, 3]
Output: True
Input: root = [5, 1, 4, null, null, 3, 6]
Output: False

    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 
        1. Def helper(node = curr node, min, max)
            1. base case: 
            empty node returns true
            2. Check if node.val is within valid range:
                min<node.val<max
            3. Recursively check left subtree
                all values must be less than current node's value
            4. Resursively check right subtree
                all values must be greater than current node's value
            5. if both subtrees are valid 
                Return true only 
                return left_is_valid and right_is_valid                       
        2. # Initialize recursion with infinite bounds
        return helper(root, float('-inf'), float('inf')) 


    I - Implement
'''

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
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode("Trunk", TreeNode('Mcintosh'), TreeNode("Granny Smith"))
root.left.left = TreeNode("Fuji") 
root.left.right = TreeNode("Opal")
root.right.right = TreeNode("Gala")
root.right.left = TreeNode("Crab")

# print_tree(root)

'''    Problem 2: Calculating Yield
    U - Understand
        I - Input - root
        O - Output - int, Return the result of evaluating the root node.
        C - constraints/considerations: exactly 3 nodes
            - The root has a string value of either "+", "-", "*", or "-".
            - Leaf nodes have an integer value.
        E - example/edge cases
    P - Plan
        High-level: use if else stmt
        Steps: 
            - 
            - 
    I - Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def calculate_yield(root):
    right = root.right.val
    left = root.left.val
    root_val = root.val
    if root_val == "+":
        return left + right
    elif root_val == "-":
        return left - right
    elif root_val == "*":
        return left * right
    else: 
        if right == 0:
            return "we cannot divide by 0"             
        else: return left / right
"""
    +
  /   \
 7     5
"""
apple_tree = TreeNode("/", TreeNode(7), TreeNode(0))
# print(calculate_yield(apple_tree))
# time and space complexity O(1)
'''    
    U - Understand
        I - Input - Given the root of the plant, 
        O - Output - return a list with the value of each node in the path from the root node to the rightmost leaf node.
        C - constraints/considerations
        E - example/edge cases
            - If there is no right child, return only the root node value (the rightmost path in this case is just the root node).
    P - Plan
        High-level: 
        Steps: 
            - create result list with root. val
            - traverse root.right, til not right child:
                add right.val to the result list
    I - Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def right_vine(root):
#     if not root:
#         return []
#     result = [root.val]
#     temp = root.right
#     while temp:
#         result.append(temp.val)
#         temp = temp.right
#     return result
def right_vine(root):
    if not root:
        return []
    return [root.val] + right_vine(root.right)

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

# print(right_vine(ivy1))
# print(right_vine(ivy2))

'''    
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
