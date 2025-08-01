from util_printing_generating_tree import print_tree, build_tree
''' 
Problem 1: Clone Detection
You have just started a new job working the night shift at a local hotel, but strange things have been happening and you're starting to think it might be haunted. Lately, you think you've been seeing double of some of the guests.

Given the roots of two binary trees guest1 and guest2 each representing a guest at the hotel, write a function that returns True if they are clones of each other and False otherwise.

Two binary trees are considered clones if they are structurally identical, and the nodes have the same values.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.   
    U - Understand
        I - Input: roots of 2 BT - 'guest1' and 'guest2'
        O - Output: True or False
        C - constraints/considerations: 
            Two binary trees are considered clones if they are structurally identical, and the nodes have the same values.
        E - example/edge cases
        HAPPY CASE
            Input: guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes")), 
                guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
            Output: True
            Explanation: The trees have identical structure and values.

            Input: guest3 = TreeNode("John Doe", TreeNode("6 ft")),
                guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))
            Output: False
            Explanation: The trees have the same values but different structures, so they are not clones.

        EDGE CASE: (both trees are empty)
            Input: guest1 = None, guest2 = None
            Output: True
            Explanation: Both trees are empty, so they are clones.
        Edge Case: only one tree is empty but not the other - 
            Input: guest1 = TreeNode("John Doe"), guest2 = None
            Output: False
            Explanation: One tree is empty, and the other is not, so they are not clones.
    P - Plan
        High-level: 
            Recursion
            Tree traversal: traverse both trees and compare the nodes at each step.
        Steps: 
        1. Base cases:
            1. if both trees are None, => T
            2. if only one of the guests is None, => F (they cannot be clones)
        2. Node comparison:
            check of the current nodes of both guests have same values
            Recursive cases:        
            1. Recursively check the left subtree of both trees
            2. Recursively check the right subtree of both guest1 and guest2
        3. return T if all checks pass, other F
    I - Implement
'''
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_clone(guest1, guest2):
    if not guest1  and not guest2:
        return True
    if guest1 is None or guest2 is None:
        return False
    '''guest1.val == guest2.val
    # Recursive cases: 
    left_is_clone =is_clone(guest1.left, guest2.left)
    right_is_clone = is_clone(guest1.right, guest2.right)
    return left_is_clone and right_is_clone'''
    # or use this alternative short circuiting method: 
    return (guest1.val == guest2.val and is_clone(guest1.left, guest2.left) and is_clone(guest1.right, guest2.right))

r""" Example Usage:
     John Doe               John Doe
     /      \             /       \
  6 ft    Brown Eyes      6ft      Brown Eyes
"""
guest1 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))
guest2 = TreeNode("John Doe", TreeNode("6 ft"), TreeNode("Brown Eyes"))

r"""
     John Doe         John Doe
     /                       \
   6 ft                     6 ft
"""
guest3 = TreeNode("John Doe", TreeNode("6 ft"))
guest4 = TreeNode("John Doe", None, TreeNode("6 ft"))

print(is_clone(guest1, guest2))
print(is_clone(guest3, guest4))
print(is_clone(None, None))

r'''
Example Output:

True
False
'''

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