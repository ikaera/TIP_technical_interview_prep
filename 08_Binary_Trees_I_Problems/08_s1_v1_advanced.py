# Week 8

'''
Problem: Cheapest Summer Getaway
You are planning a trip across a grid of cities. You start at the top-left city (0, 0) and want to reach the bottom-right city (m-1, n-1), which is your final vacation destination.

Each cell in the grid represents the layover tax or transit fee for that city. You can only move down or right at any point in time.

Return the minimum total cost to reach your destination.

Example:

Input: grid = [ [1, 3, 1], [1, 5, 1], [4, 2, 1] ]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum. (1+3+1+1+1 = 7).
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

Problem 1: Ivy Cutting
You have a trailing ivy plant represented by a binary tree. You want to take a cutting to start a new plant using the rightmost vine in the plant. Given the root of the plant, return a list with the value of each node in the path from the root node to the rightmost leaf node. If there is no right child, return only the root node value (the rightmost path in this case is just the root node).

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U - Understand
    I - Input - root of the plant
    O - Output - return a list with the value of each node in the path from the root node to the rightmost leaf node
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

def right_vine(root):
    #base case is empty
    if not root: return []
    #return root.val + recursive call on right child
    return [root.val] + right_vine(root.right)

# complexity space and time is O(height)

# 2 problem
def right_vine_iter(root):
    # init list
    result = []
    # traverse to the tree
    temp = root
    while temp: 
        result.append(temp.val)
        temp = temp.right
    return result

r"""
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

# print(right_vine_iter(ivy1))
# print(right_vine_iter(ivy2))
# Example Output:
# ['Root', 'Node2', 'Leaf3']
# ['Root']

# Problem 3

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def survey_tree(root):
    # base case:
    if not root:
        return []
    # recursive cases:
    #1) traverse the current node's left subtree
    #2) traverse the current node's right subtree
    # visit the current node
    return survey_tree(root.left) + survey_tree(root.right) + [root.val]
    
# Example Usage:
r"""
        Root
      /      \
    Node1    Node2
  /         /    \
Leaf1    Leaf2  Leaf3
r"""
magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
# print(survey_tree(magnolia))
# Example Output: ['Leaf1', 'Node1', 'Leaf2', 'Leaf3', 'Node2', 'Root']

# problem 4
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    """"""
    if not inventory: 
        return 0
    #value + left + right
    return inventory.val + sum_inventory(inventory.left) + sum_inventory(inventory.right)


# Example Usage:

r"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))

# Problem 5: Calculating Yield II

'''    
U - Understand
    I - Input
    O - Output - Return the result of evaluating the root node. 
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

# def calculate_yield(root):
    # base case: leaf node return value
    

'''
'''