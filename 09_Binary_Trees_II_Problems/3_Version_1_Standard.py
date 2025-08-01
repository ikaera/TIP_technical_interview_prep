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
# print_tree(merge_orders(order1, order2))
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
        According to ChatGPT: 
        Final Space Complexity (Call Stack)
        For a balanced binary tree (height is log n)
        If the tree were unbalanced or skewed, it could be O(n) in the worst case
        (think critically about the advantages and disadvantages of your chosen approach).

    https://chat.deepseek.com/a/chat/s/af3487ee-789c-493b-bb2a-904d0f7be0d3
    Function: merge_orders(order1, order2)
    !!Termination Conditions: 
        If either tree is exhausted (None), the recursion stops for that branch =>  
        This means we only traverse nodes that exist in both trees!!
    Time Complexity: O(min(N₁, N₂)) where:
        N₁ = number of nodes in order1
        N₂ = number of nodes in order2
    Space Complexity: O(min(N₁, N₂))
        New tree creation requires O(min(N₁, N₂)) space
        Recursion stack depth is O(log(min(N₁, N₂))) for balanced trees
    Key insight: the algorithm's efficiency comes from:
        1. Only processes the overlapping nodes
        2. Constant time operations per node
        3. Recursion depth is limited by smaller tree size
'''

#####################################
'''   
## Problem 2: Croquembouche
You are designing a delicious croquembouche (a French dessert composed of a cone-shaped tower of cream puffs 😋), for a couple's wedding. They want the cream puffs to have a variety of flavors. You've finished your design and want to send it to the couple for review.

Given a root of a binary tree design where each node in the tree represents a cream puff in the croquembouche, that prints a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level).

Note: The build_tree() and print_tree() functions both use variations of a level order traversal. To get the most out of this problem, we recommend that you reference these functions as little as possible while implementing your solution.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.
 
U - Understand
    I - Input = a root of a binary tree design
    O - Output = a list of the flavors (vals) of each cream puff in level order (i.e., from left to right, level by level)
    C - constraints/considerations
    E - example/edge cases
        HAPPY CASE
        Input: croquembouche = Puff("Vanilla", Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), Puff("Strawberry"))
        Output: ['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
        Explanation: The flavors are printed level by level, starting from the root.

        Input: croquembouche = Puff("Chocolate")
        Output: ['Chocolate']
        Explanation: The tree has only one node, so return its flavor.

        EDGE CASE
        Input: croquembouche = None
        Output: []
        Explanation: The tree is empty, so return an empty list.

        Input: croquembouche = Puff("Vanilla", Puff("Chocolate"), None)
        Output: ['Vanilla', 'Chocolate']
        Explanation: The tree has only two nodes, and the second node is on the left.
P - Plan
    High-level: Breadth First Search Traversal, use deque

    Steps: 
    1. if tree is empty return an empty list (if design is None )
    2. Init a queue with `design` as its fist el and 
    3. Init an empty result list 
    4. while loop (queue):
        a. using `popleft()` dequeue the first node in the queue and 
        b. append `node's val` to the `result` list 
        c. if node has a left child, append it to the queue 
        d. if node has a right child, append it to the queue
    5. outside of the loop print(result)
I - Implement
'''
from collections import deque
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def print_design(design):
    if not design:
        return []
    double_ended_queue = deque([design])
    result = []
    while double_ended_queue:
        cur_node = double_ended_queue.popleft()
        result.append(cur_node.val)
        if cur_node.left:
            double_ended_queue.append(cur_node.left)
        if cur_node.right:
            double_ended_queue.append(cur_node.right)    
    print(result)

r"""
Example Usage:
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))
croquembouche0 = Puff(None)
croquembouche1 = Puff("Vanilla", Puff("Chocolate"), None)
croquembouche2 = Puff("Vanilla",  None, Puff("Chocolate"))
# print_design(croquembouche)
# print_design(croquembouche0)
# print_design(croquembouche1)
# print_design(croquembouche2)

'''
Example Output:

['Vanilla', 'Chocolate', 'Strawberry', 'Vanilla', 'Matcha']
'''
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''
####################################
'''
Problem 3: Maximum Tiers in Cake
You have entered your bakery into a cake baking competition and for your entry have decided build a complicated pyramid shape cake, where different sections have different numbers of tiers. Given the root of a binary tree cake where each node represents a different section of your cake, return the maximum number of tiers in your cake.

The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time complexity. Assume the input tree is balanced when calculating time complexity.


U - Understand
    I - Input `cake` - root of the tree
    O - Output = int. the maximum number of tiers
    C - constraints/considerations
        The maximum number of tiers is the number of nodes along the longest path from the root node down to the farthest leaf node.
    E - example/edge cases
        HAPPY CASE
        Input: cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
        Output: 3
        Explanation: The longest path is from "Chocolate" -> "Strawberry" -> "Coffee".

        Input: cake_sections = ["Vanilla"]
        Output: 1
        Explanation: The tree has only one node, so the maximum number of tiers is 1.

        EDGE CASE
        Input: cake_sections = []
        Output: 0
        Explanation: The tree is empty, so return 0.

        Input: cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, "Raspberry"]
        Output: 3
        Explanation: The longest path is from "Chocolate" -> "Vanilla" -> "Raspberry".
P - Plan
    High-level: 
        DFS adn  
        Recursion
    Steps: 
    Base case:
        1. 
    Recursive depth calc.:
        2.

I - Implement
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def max_tiers(cake):
    if cake is None:
        return 0
    # recursive
    right_depth = max_tiers(cake.right)
    left_depth  = max_tiers(cake.left)
    return 1 + (max(right_depth, left_depth))

# Iterative approach
'''
M Match: 
    BFS 
    Level Order Traversal: Traverse the tree level by level and increment the depth counter for each level processed.
P Plan
    steps:
        1. if tree is empty (None) return 0
        2. 
        3.
        4.  
'''
def max_tiers_iter(root):
    if root is None:
        return 0
    # 2
    queue = deque([root])
    num_tiers = 0
    # BFS
    while (queue):
        # Determine the number of nodes at the current level (level_size).
        level_size = len(queue)
        for i in range(level_size):                         
            node = queue.popleft()
            print(node.val)                            
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)                
        num_tiers += 1
        
    return num_tiers

# Example Usage:
r"""
        Chocolate
        /        \
    Vanilla    Strawberry
                /     \
         Chocolate    Coffee
"""
# Using build_tree() function included at top of page
cake_sections = ["Chocolate", "Vanilla", "Strawberry", None, None, "Chocolate", "Coffee"]
cake = build_tree(cake_sections)

# print(max_tiers(cake))
# print(max_tiers(None))

print(max_tiers_iter(cake))
print(max_tiers_iter(None))
# Example Output: 3
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