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

# print(max_tiers_iter(cake))
# print(max_tiers_iter(None))
# Example Output: 3

'''

R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''
##############################
r'''    
Problem #1: Given the root of a binary tree and an integer target_sum, return True if the tree has a root-to-leaf path such that adding up all the values along the path equals target_sum. A leaf is a node with no children.

U - Understand
    I - Input - root: TreeNode, targetSum: int
    O - Output - T / F 
    C - constraints/considerations
    E - example/edge cases
            5
            / \
        4   8
        /   / \
        11  13  4
        / \      \
        7   2      1
        target_sum = 22
        Output: True
        -------------
            1
            / \
            2   3
            target_sum = 5
            Output: False
            ------------
                1
                target_sum = 1
                Output: True
                ------------------
M — Match with Patterns
    Interviewer Prompts & Possible Answers:
    "What kind of traversal do you think fits best here?"
    → "Depth-first search makes sense since we're exploring complete paths from root to leaves."

    "Have you seen problems involving root-to-leaf paths before?"
    → "Yes, similar to problems like path sum collection, max depth, or binary tree path listing."

    "Do you think recursion or iteration would work better for this?"
    → "Recursion feels more natural because the structure of the problem mirrors the recursive tree traversal. Iteration would need a stack and extra bookkeeping."

    "What's the key insight for solving this recursively?"
    → "At each node, we reduce the problem by subtracting the current node's value from the target and recursing on children."

P - Plan
    High-level: At each node, subtract the current node's value from the target. If we reach a leaf and the remaining sum is zero, we return true.
        - Start at the root. If the tree is empty, return False.
        - If you're at a leaf, check if the leaf's value matches the remaining target sum.
        - If not at a leaf, subtract the current node's value from the target sum and repeat the process for the left and right children.
        - If either child returns True, the answer is True.
    Steps: 
        "1. Handle null tree case. 2. Check if current node is a leaf and equals remaining target. 3. Recursively check left and right subtrees with updated target. 4. Return true if either subtree has a valid path."
    Base cases: 
        1. (Empty tree) if root is None, that means tree is empty return False, 
            because there is no path to consider.
        2. (Leaf node check) if the current node is leaf (both root.left and root.right are None)
            check if node' value == the remaining `target_sum`
            if yes return True otherwise False
    Recursive cases:
        3. if the current node is not a leaf, to get remaining_sum = target_sum - node's value
        4. Recursively check the left and right subtree with the updated remaining_sum
        Return true if either subtree has a valid path (use `or` operator not and )
I - Implement
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root: TreeNode, target_sum: int) -> bool:
    if root is None: # Base case:
        return False
    if root.left is None and root.right is None:
        return root.val == target_sum
    else: # Recursive cases: 
        remaining_sum = target_sum - root.val
        left_path = hasPathSum(root.left, remaining_sum)
        right_path = hasPathSum(root.right, remaining_sum)
    return left_path or right_path
'''
# Test 1: Empty tree
print(hasPathSum(None, 0))  # Expected: False

# Test 2: Single node that matches target
print(hasPathSum(TreeNode(5), 5))  # Expected: True

# Test 3: Single node that doesn't match
print(hasPathSum(TreeNode(3), 5))  # Expected: False

# Test 4: Simple left path (1 -> 2 = 3)
tree = TreeNode(1, TreeNode(2))
print(hasPathSum(tree, 3))  # Expected: True

# Test 5: Simple right path (1 -> 3 = 4)
tree = TreeNode(1, None, TreeNode(3))
print(hasPathSum(tree, 4))  # Expected: True

# Test 6: No matching path
tree = TreeNode(1, TreeNode(2), TreeNode(3))
print(hasPathSum(tree, 5))  # Expected: False
'''
'''
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''

''' 
Problem #2
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
U - Understand
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/edge cases
P - Plan
    High-level: 

    Steps: 1. Check if both nodes are null (same). 2. Check if one is null but not the other (different). 3. Check if values are different (different). 4. Recursively check left subtrees and right subtrees.

I - Implement
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isSameTree(p, q):
    # base cases:
    if not p and not q:
        return True
    # Base case:
    if not p or not q:
        return False
    # base case
    if q.val != p.val:
        return False
    # recursive cases: left and right subtrees
    left_is_same = isSameTree(p.left, q.left)
    right_is_same = isSameTree(p.right, q.right)

    return left_is_same and right_is_same

# R- Review
def test_isSameTree():
    # Both empty
    # print("Test 1: Both trees None")
    assert isSameTree(None, None) == True
    print("[OK] Passed Test 1: Both trees None")
    
    # One empty, one not
    assert isSameTree(None, TreeNode(1)) == False
    assert isSameTree(TreeNode(1), None) == False
    
    # Single nodes - same
    assert isSameTree(TreeNode(1), TreeNode(1)) == True
    
    # Single nodes - different
    assert isSameTree(TreeNode(1), TreeNode(2)) == False
    
    # Same structure and values
    tree1 = TreeNode(1, TreeNode(2), TreeNode(3))
    tree2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert isSameTree(tree1, tree2) == True
    
    # Same values, different structure
    tree3 = TreeNode(1, TreeNode(2), None)
    tree4 = TreeNode(1, None, TreeNode(2))
    assert isSameTree(tree3, tree4) == False
    
    # Different values
    tree5 = TreeNode(1, TreeNode(2), TreeNode(1))
    tree6 = TreeNode(1, TreeNode(1), TreeNode(2))
    assert isSameTree(tree5, tree6) == False
    print("All test cases passed!")

test_isSameTree()
'''
E - evaluate 
Time: O(min(m,n)) where m and n are the number of nodes in each tree, since we stop as soon as we find a difference. Space: O(min(m,n)) for recursion stack in worst case.
    - Time  complexity: O(nim(m,n))
    - Space complexity: O(min(m,n))
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
R- Review

E - evaluate 
    - Time  complexity:
    - Space complexity:
        (think critically about the advantages and disadvantages of your chosen approach).
'''
###############################
''' 
Problem Set Version 2  Clone Detection
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

# print(is_clone(guest1, guest2))
# print(is_clone(guest3, guest4))
# print(is_clone(None, None))

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