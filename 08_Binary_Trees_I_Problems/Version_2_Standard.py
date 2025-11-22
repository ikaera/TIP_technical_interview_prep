
# Testing your Binary Tree (Printing)
from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root
# print_tree(root)
# print_tree(None)

'''    
U - Understand
    I - Input - root of the bt
    O - Output - int = the number of Monstera leaves 🍃 that have an odd number of splits.
    C - constraints/considerations
    E - example/edge cases
P - Plan
    High-level: traverse the bt and increase the count if val is odd. 
    Steps: 
        base case: if root is null, return 0
        if root.val %2 != 0:
        count += 1
        recursive case: 
        left_odd_count = count_odd_splits(root.left)
        right_odd_count = count_odd_splits(root.right)
    return count + left_odd_count + right_odd_count
I - Implement
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def count_odd_splits(root):
    if root is None: 
        return 0
    count = 0
    if root.val %2 != 0:
        count += 1
    left = count_odd_splits(root.left)
    right = count_odd_splits (root.right)
    return count + left + right 

# Using build_tree() function included at top of page
values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

# print(count_odd_splits(monstera))
# print(count_odd_splits(None))


## PROBLEM 2: Flower Finding



'''Problem 2: Flower Finding
U - Understand: If a flower is in the BST, return true, return false otherwise.

    I - Input:
        Inventory (the root of BST), and name the desired flower in inventory.
    O - Output:
        T/F
    C - constraints/considerations: Balanced 
    E - example/edge cases
        Empty tree, Desired flower is an empty string
P - Plan
    High-level: 
            Iteratively / recursively, order (in-order, pre-order, and post-order)
                - Recursively 
                Start with case, if Root is None return false, starting with root value, return true
                If name is less or greater, go left
                if name is greater, go right
            
    Steps: 
          Base Case:
                    If Root is None:
                        Return False
        If inventory.val == name:
            return True
        elif inventory.val <= name:
            return find_flower(inventory.right, name)
        elif inventory.val > name:
                return find_flower(inventory.left, name)

I - Implement
'''
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if not inventory:
        return False
    
    if inventory.val == name:
        return True
    elif inventory.val <= name:
        return find_flower(inventory.right, name)
    elif inventory.val > name:
        return find_flower(inventory.left, name)
"""
         Rose
        /    \
      Lilac   Tulip
     /  \       \
  Daisy  Lily  Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]

garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 

        
'''Problem 3: Flower Finding II
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

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)

'''    
U - Understand
    I - Input
        inventory - root of a binary tree
        name - name of a flower
    O - Output 
        boolean - T/F if flower node with name exists in the tree
    C - constraints/considerations
        - not a binary search tree
    E - example/edge cases
        - root is null
        - name is an empty string
1. Compare:
2. Time complexity: O
3. Time complexity:

'''

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def non_bst_find_flower(root, name):
    if root is None:
        return False
    
    if root.val == name:
        return True

    return non_bst_find_flower(root.left, name) or non_bst_find_flower(root.right, name)