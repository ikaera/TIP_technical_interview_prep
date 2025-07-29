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
Problem 4: Documenting Reefs
You are exploring a vast coral reef system. The reef is represented as a binary tree, where each node corresponds to a specific coral formation. You want to document the reef as you encounter it, starting from the root or main entrance of the reef.

Write a function explore_reef() that performs a preorder traversal of the reef and returns a list of the names of the coral formations in the order you visited them. In a preorder exploration, you explore the current (root) node first, then the left subtree, and finally the right subtree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.

U-nderstand:
    I - Input root 
    O - Output - returns a list of the names of the coral formations
    C - constraints/considerations - preorder exploration, you explore the current node first, then the left subtree, and finally the right subtree.
    E - example/
    edge cases - empty tree will return an empty list
M-atch: Rescurisve preorder traversal
P-lan:
    High-level: 

    Steps: 
        1. Base case: root(current Node) is None, retun [] empty list 
        2. start visiting root node and store its value to result
        3. Rescursive case: 
            1. traverse the left subtree and collect its values
            2. traverse right subtree and collect its values
        4. return result
I-Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

'''def explore_reef(root):
    # init empty list
    result = []
    # base case: 
    if root is None:
        return []
    # visit root node
    result.append(root.val)
    # recursive cases: 
    # 1. recur left subtree
    result += explore_reef(root.left)
    # 2. recur right subtree
    result += explore_reef(root.right)
    return result
'''
'''
Plan: with helper function
    1. In the main function, initialize the result list
    2. Inside the main function, define a helper function - 
        helper(node, result)
        1. Base case: Handle the base case inside helper
            If node is None, return (do nothing)
        2. Visit the current node,
            Add node.val to the result list
        2 recur cases
        3. Recur on the left child
        4. Recur on the right child
    3. Call the helper function starting from the root
    4. Return the final result list
'''
def explore_reef(root):
    result = []
    def helper(node, result):
        # base case
        if node is None:
            return []
        result.append(node.val)
        # recur case:
        helper(node.left, result) 
        helper(node.right, result)       
    helper(root, result)
    return result

'''def explore_reef_iter(root):
    # If the tree is empty, return an empty list
    if root is None:
        return []
    # Initialize a stack with the root node to begin traversal
    stack = [root]
    # This will store the visited node values in pre-order
    result = [] 
    
    while stack: # Continue while there are nodes to process
        # Pop the top node from the stack (LIFO order)
        currrent = stack.pop()
        # Visit the current node by adding its value to the result
        result.append(currrent.val)

        # Push right child first (so it's processed after left)
        if currrent.right:
            stack.append(currrent.right) # rgiht child goes second in stack (LIFO order)

        # Push left child next (so it's processed first)
        if currrent.left:
            stack.append(currrent.left) # Left child goes on top of stack

    # Once the stack is empty, return the full list of visited node values
    return result
'''
# Example Usage:

"""
           
"""

reef = TreeNode("CoralA", 
                TreeNode("CoralB", TreeNode("CoralD"), TreeNode("CoralE")), 
                          TreeNode("CoralC"))
print(explore_reef(reef))
# print(explore_reef_iter(reef))
'''Example Output:

['CoralA', 'CoralB', 'CoralD', 'CoralE', 'CoralC']
'''
reef1 = TreeNode("CoralA")
# print(explore_reef(reef1))

reef2 = TreeNode(None)
# print(explore_reef(reef2))