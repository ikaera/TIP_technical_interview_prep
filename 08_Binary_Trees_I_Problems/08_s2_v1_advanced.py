# w8s2v1
# Returns the root of the binary tree made from values.
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
# Example Usage:

r"""
          1
        /   \
       2     3
      /     / \
     4     5   6
"""

tree_with_just_values = [1, 2, 3, 4, None, 5, 6]
val_tree = build_tree(tree_with_just_values)

"""
          (1, 'A')
          /       \
       (2, 'B')   (3, 'C')
      /           /      \
  (4, 'D')    (5, 'E')   (6, 'F')
"""

tree_with_keys_and_values = [(1, 'A'), (2, 'B'), (3, 'C'), (4, 'D'), None, (5, 'E'), (6, 'F')]
key_val_tree = build_tree(tree_with_keys_and_values)

# Using print_tree() function included above 
# print_tree(val_tree)
# print_tree(key_val_tree) # Only values will be printed
# Example Output:
# [1, 2, 3, 4, None, 5, 6]
# ['A', 'B', 'C', 'D', None, 'E', 'F']
#####################################
#####################################

'''Problem Set Version 1 ###
######### - Problem 1: Sorting Plants by Rarity
You are going to a plant swap where you can exchange cuttings of your plants for new plants from other plant enthusiasts. You want to bring a mix of cuttings from both common and rare plants in your collection. You track your plant collection in a binary search tree (BST) where each node has a key and a val. The val contains the plant name, and the key is an integer representing the plant's rarity. Plants are organized in the BST by their key.

To help choose which plants to bring, write a function sort_plants() which takes in the BST root collection and returns an array of plant nodes as tuples in the form (key, val) sorted from least to most rare. Sorted order can be achieved by performing an inorder traversal of the BST.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, key, val, left=None, right=None):
        self.key = key      # Plant rarity
        self.val = val      # Plant name
        self.left = left
        self.right = right


def sort_plants(collection):
    pass
# Example Usage:

r"""
         (3, "Monstera")
        /               \
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

# print(sort_plants(collection))

# # Example Output:
# [(1, 'Pothos'), (2, 'Spider Plant'), (3, 'Monstera'), (4, 'Hoya Motoskei'), (5, 'Witchcraft Orchid')]


'''
######### - Problem 2: Flower Finding #########
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in a binary search tree (BST) where each node represents a plant in the store. The plants are organized according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() that returns True if the flower is present in the garden and False otherwise.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
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
    elif name < inventory.val:
      return find_flower(inventory.left, name)
    else: 
      return find_flower(inventory.right, name)
# Example Usage:

r"""
         Rose
        /    \
      Lily   Tulip
     /  \       \
  Daisy  Lilac  Violet

"""

# using build_tree() function at top of page
values = ["Rose",  "Tulip", "Daisy", "Lilac", "Lily", None, "Violet"]
garden = build_tree(values)

# print(find_flower(garden, "Lilac"))  
# print(find_flower(garden, "Sunflower")) 
# Example Output:
# True
# False

'''
######### - Problem 3: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! Your collection is meticulously organized using a Binary Search Tree (BST) where each node in the tree represents a houseplant in your collection, and houseplants are organized alphabetically by name (val).

Given the root of your BST collection and a new houseplant name, insert a new node with value name into your collection. Return the root of your updated collection. If another plant with name already exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    pass
# Example Usage:

r"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
# print_tree(add_plant(collection, "Aloe"))
# Example Output:
# ['Money Tree', 'Fiddle Leaf Fig', 'Snake Plant', 'Aloe']

'''Explanation: 
Tree should have the following structure:
           Money Tree
        /              \
 Fiddle Leaf Fig   Snake Plant
   /
 Aloe'''

'''
######### - Problem 4: Remove Plant
A plant in your houseplant collection has become infested with aphids, and unfortunately you need to throw it out. Given the root of a BST collection where each node represents a plant in your collection, and a plant name, remove the plant node with value name from the collection. Return the root of the modified collection. Plants are organized alphabetically in the tree by value.

If the node with name has two children in the tree, replace it with its inorder predecessor (rightmost node in its left subtree). You do not need to maintain a balanced tree.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def remove_plant(collection, name):
    pass
# Example Usage:

r"""
              Money Tree
             /         \
           Hoya        Pilea
              \        /   \
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
# print_tree(remove_plant(collection, "Pilea"))

# Example Output:
# ['Money Tree', 'Hoya', 'Orchid', None, 'Ivy', None, 'ZZ Plant']
r'''
Explanation:
The resulting tree structure:
             Money Tree
            /         \
          Hoya       Orchid
              \          \
              Ivy      ZZ Plant
💡 Hint: Inorder Predecessor
'''
'''
######### - Problem 5: Find Most Common Plants in Collection
You have a vast plant collection and want to know which plants you own the most of. Given the root of a BST with duplicates where each node is a plant in your collection, return a list with the name(s) (val) of the most frequently occurring plant(s) in your collection. If multiple plants tie for the most frequently occuring plant, you may return them in any order.

Assume your BST organizes plants alphabetically by name and follows the following rules:

The left subtree of a node contains only nodes with values less than or equal to the node's value
The right subtree of a node contains only nodes with values greater than or equal to the node's value.
Both the left and right subtrees must also be BSTs.
Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def find_most_common(root):
    pass
# Example Usage:

r"""
    Hoya
      \ 
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

r"""
      Hoya
    /      \ 
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

# print(find_most_common(collection1))
# print(find_most_common(collection2))
# Example Output:
# ['Pothos']
# ['Aloe', 'Pothos']
# 💡 Hint: Choosing a Traversal Order
'''
######### - Problem 6: Split Collection
You've accumulated too many plants, and need to split up your collection. Given the root of a BST collection where each node represents a plant in your collection and a value target, split the tree into two subtrees where the first subtree has node values that are lexicographically (alphabetically) smaller than or equal to target and the second subtree has all nodes that are greater than target. It is not necessarily the case that the collection contains a plant (node) with value target.

Additionally, most of the structure of the original tree should remain. Formally for any child plant c with parent p in the original collection, if they are both in the same subtree/subcollection after teh split, then plant c should still have the parent p.

Return an array of the two root nodes of the two subtrees in order.

Evaluate the time and space complexity of your function. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity. Assume the input tree is balanced when calculating time and space complexity.
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def split_collection(collection, target):
    pass
# Example Usage:

# Example input BST 'collection'

r"""
              Money Tree
             /         \
           Hoya        Pilea
           /   \        /   \
        Aloe   Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of the page
values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of the page
# left, right = split_collection(collection, "Hoya")
# print_tree(left)
# print_tree(right)

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