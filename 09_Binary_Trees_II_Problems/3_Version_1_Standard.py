from util_printing_generating_tree import print_tree, build_tree
"""
# Standard Problem Set Version 1
## Problem 1: Merging Cookie Orders

You run a local bakery and are given the roots of two binary trees `order1` and `order2` where each node in the binary tree represents the number of a certain cookie type the customer has ordered. To maximize efficiency, you want to bake enough of each type of cookie for both orders together.

Given order1 and order2, merge the order together into one tree and return the root of the merged tree. To merge the orders, imagine that when place one tree on top of the other, some nodes of the two trees are overlapped while others are not. If two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the not None node will be used as the node of the new tree.

Start the merging process from the root of both orders.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
 
    U - Understand
        I - Input = `order1` and `order2`
        O - Output = return the the root of the merged tree
        C - constraints/considerations
            Start the merging process from the root of both orders.
        E - example/edge cases
        Q&A:
        -What should be returned if one of the trees is None?
            Return the other tree since there are no nodes to merge from the None tree.
        -What if both trees are None?
            Return None since there are no nodes in either tree.
        -Are the trees guaranteed to be balanced?
            The problem assumes the input trees are balanced when calculating time complexity.
    P - Plan
        High-level: Traverse both trees,
            DFS, pre-order traversal may be best since we have to start the merging process from the root of both orders, 
            Thus, first root node => left and right subtree.
        Steps: 
        1. Base case: 
            if either order is None return the other tree
        2. Init new node `merged_node`, with the value = order1.val + oder2.val
        3. Recursive cases: Recursively merge the left and right children  
            1. Left
                - recursively call merge_orders func passing left children of both trees(order1 and order2)
                - assign the result to the me_node's left child
            2. Right
                - recursively call merge_orders func passing right children of both trees
                - assign the result to the right child of the merged_node
        4. return the merged_node
    I - Implement
"""
class TreeNode():
     def __init__(self, quantity, left=None, right=None):
        self.val = quantity
        self.left = left
        self.right = right

def merge_orders(order1, order2):
    # step 1
    if order1 is None:
        return order2
    if order2 is None:
        return order1
    # step 2 merge the nodes
    sum = order1.val + order2.val
    merged_node = TreeNode(sum)
    # step 3 Recursive cases:
    merged_node.left = merge_orders(order1.left, order2.left)
    merged_node.right = merge_orders(order1.right, order2.right)
    # step 4:
    return merged_node
r"""
Example Usage:
     1             2         
    /  \         /   \       
   3    2       1     3   
 /               \      \   
5                 4      7   
"""
# Using build_tree() function included at top of page
cookies1 = [1, 3, 2, 5]
cookies2 = [2, 1, 3, None, 4, None, 7]
order1 = build_tree(cookies1)
order2 = build_tree(cookies2)

# Using print_tree() function included at top of page
print_tree(merge_orders(order1, order2))
r'''
Example Usage:

[3, 4, 5, 5, 4, None, 7]
Explanation:
Merged Tree:
     3
    /  \      
  4     5  
 / \      \
5   4      7
'''
r'''
# Test Case: Both trees are None
order1 = None
order2 = None
result = merge_orders(order1, order2)
print_tree(result)  # Output: Empty


# Test Case 2: One empty tree
tree1 = build_tree([1, 2, 3])
tree2 = None
print_tree(merge_orders(tree1, tree2))  # Output: [1, 2, 3]

# Test Case 3: Simple symmetric merge
tree1 = build_tree([1, 2, 3])
tree2 = build_tree([4, 5, 6])
print_tree(merge_orders(tree1, tree2))  # Output: [5, 7, 9]

# Test Case 4: Different tree shapes
tree1 = build_tree([1, 2, None, 3])
tree2 = build_tree([4, None, 5])
print_tree(merge_orders(tree1, tree2))  # Output: [5, 2, 5, 3]
'''
'''
------------------------

R- Review

E - evaluate n is num of node and h is height of the treen since it is balanced h = log(n)
    - Time  complexity: O(n) because each node must be visited once
    - Space complexity: O(n) due to the recursive call stack and the n space required to create the merged tree.
        (think critically about the advantages and disadvantages of your chosen approach).
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
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
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
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
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
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
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
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
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
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''