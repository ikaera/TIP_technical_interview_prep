from util_printing_generating_tree import print_tree, build_tree

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
'''  
Problem 1: Balanced Baked Goods Display
    U - Understand
        I - Input - Given the root of a binary tree display
        O - Output - return True if the tree is balanced and False otherwise.
        C - constraints/considerations
        E - example/edge cases - no root => true
        definition: 
        A balanced display is a binary tree in which the difference in the height of the two subtrees of every node never exceeds one.
    P - Plan
        High-level: 
        Steps: 
        - 
        - def helper(root):
            - Base case: if not root => true, 0
            - Recursive cases: 
                - left_bal,  left_sub_height = helper(root.left)
                - right_bal, right_sub_height = helper(root.right)
            - bal = abs(left_sub_height - right_sub_height) <= 1
            return bal, (max(left_sub_height, right _sub_height) +1)  
        - balanced = helper(display) 
        return balanced

    I - Implement
'''
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_balanced(display):
    # edge case:
    if not display:
        return True
    # recursive case: 

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