# Week 9

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

'''
Problem 1: Croquembouche II
U - Understand
    I - Input - binary tree
    O - Output - list of list
    C - constraints/considerations: Assume the input tree is balanced 
    E - example/edge cases 
        binary tree is empty => empty list

P - Plan
    High-level: Hint: Level order traversal, BFS
    Steps: 
BFS
If the tree is empty:
    return an empty list

Create an empty queue
Create an empty list to store visited nodes

Add the root into the queue

While the queue is not empty:
    Pop the next node off the queue 
    Add the popped node to the list of visited nodes

    Add the popped node's left child to the queue
    Add the popped node's right child to the queue
I - Implement
'''
class Puff():
     def __init__(self, flavor, left=None, right=None):
        self.val = flavor
        self.left = left
        self.right = right

def listify_design(design):
    if not design:
        return []
    queue = deque()
    visited = []  # result list
    queue.append(design)

    while queue:
        each_level = [] # sublist at each level

        for _ in range ( len(queue)):
            node = queue.popleft()
            each_level.append(node.val)
            # visited.append(node)
            if node.left:
                queue.append(node.left)
            if node.right: 
                queue.append(node.right)

        visited.append(each_level)
    
    return visited   

r"""
            Vanilla
           /       \
      Chocolate   Strawberry
      /     \
  Vanilla   Matcha  
"""
croquembouche = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry"))

croquembouche1 = Puff("Vanilla")
croquembouche2 = None
croquembouche3 = Puff("Vanilla", 
                    Puff("Chocolate", Puff("Vanilla"), Puff("Matcha")), 
                    Puff("Strawberry", Puff("Cherry"), Puff("Banana")))

# print(listify_design(croquembouche))
# print(listify_design(croquembouche1))
# print(listify_design(croquembouche2))
# print(listify_design(croquembouche3))

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
'''