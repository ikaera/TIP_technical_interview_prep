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
Problem 4: Sum Inventory
A local flower shop stores its inventory in a binary tree, where each node represents their current stock of a flower variety. Given the root of a binary tree 'inventory', return the sum of all the flower stock in the store.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input - 
        the root of a binary tree inventory
    O - Output 
        return the sum of all the flower stock in the store.
    C - constraints/considerations
            Assume the input tree is balanced when calculating time and space complexity
    E - example/edge cases
        HAPPY CASE
        Input: Binary tree with nodes [45, 12, 10, 20, 1, 15]
        Output: 106
            Explanation: The sum of all nodes is 45 + 12 + 10 + 20 + 1 + 15 = 106.

        EDGE CASE
        Input: Binary tree with only one node [50]
        Output: 50
            Explanation: The tree has only the root, so the sum is 50.
        edge cases
        How should the function behave if the tree is empty?
            The function should return 0 if the tree is empty.
M-atch:
P-lan:
    High-level: Traverse the tree recursively, summing the values of each node by adding the sum of the left subtree and the right subtree.

    Steps: 
        1. Base case: if root is None return 0
        2. Recursive case:
            1.  right_sum = sum_inventory(inventory.right)
            2.  left_sum = sum_inventory(inventory.left)
        3. return value of root + sum of left subtree + sum of right subtree   

I-Implement
'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def sum_inventory(inventory):
    # Base case:
    if not inventory: 
        return 0
    
    # recursive case
    right_sum = sum_inventory(inventory.right)
    left_sum = sum_inventory(inventory.left)

    return right_sum + left_sum + inventory.val
# Example Usage:

"""
     40
    /  \
   5   10
  /   /  \
20   1   30
"""

# time  O(n)
# space O()
inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print("Binary tree with nodes [45, 12, 10, 20, 1, 15] => Output:", sum_inventory(inventory),"\n")
print("The tree with only one TreeNode(1)  => Output:", sum_inventory(TreeNode(1)), "\n")
print("The empty tree  => Output:", sum_inventory(None))
'''
Example Output: 106'''