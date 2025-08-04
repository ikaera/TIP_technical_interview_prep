from util_printing_generating_tree import print_tree, build_tree 
'''    
Problem 6: Maximum Icing Difference
In your bakery, you're planning a display of cupcakes where each cupcake is represented by a node in a binary tree. The sweetness level of the icing on each cupcake is stored in the node's value. You want to identify the maximum icing difference between any two cupcakes where one cupcake is an ancestor of the other in the display.

Given the root of a binary tree representing the cupcake display, find the maximum value v for which there exist different cupcakes a and b where v = |a.val - b.val| and a is an ancestor of b.

A cupcake a is an ancestor of b if either any child of a is equal to b, or any child of a is an ancestor of b.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time complexity.

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

class TreeNode():
    def __init__(self, sweetness, left=None, right=None):
        self.val = sweetness
        self.left = left
        self.right = right

def max_icing_difference(root):
    pass
# Example Usage:

r"""
            8
           /  \
         3     10
        / \      \
       1   6     14
          /  \    /
         4    7  13
"""

# Using build_tree() function included at top of page
sweetness_levels = [8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 13]
display = build_tree(sweetness_levels)

print(max_icing_difference(display))
'''
Example Output:  13
Explanation: The maximum icing difference is between the root cupcake (8) and a descendant with
sweetness level 1, yielding a difference of |8 - 1| = 7.
'''
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''