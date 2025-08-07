from collections import deque

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
The pseudocode for BFS is as follows:

    - Initialize an empty list of visited nodes
    - Initialize an empty queue 
    - Add the node we would like to start our traversal from to the queue 
    - Add the node we would like to start our traversal from to visited
    - While the queue is not empty:
        - Remove an element from the queue and store it in a variable, `current`
        - Loop through each of the current node's neighbors:
            - If the neighbor has not yet been visited:
                - Add the neighbor to the queue
                - Add the neighbor to the list of visited nodes
    - Return the list of visited nodes

#############################
The pseudocode for DFS is as follows:

- Initialize an empty stack
- Initialize an empty list to store visited nodes
- Add the node we would like to start our traversal from to the stack
- while the stack is not empty:
    - Pop the topmost node off the stack and store it in a variable, `current`
    - If the node is not already in the list of visited nodes:
        - Add `current` to the list of visited nodes
    - Loop through the current node's neighbors:
        - If the neighbor has not yet been visited
            - Push the neighbor onto the stack
- Return list of visited nodes

The pseudocode for recursive DFS is as follows:
- Main function
    def dfs(self, start_node):
        - Create empty list to store nodes that have been visited
        - Pass list of visited nodes and `start_node` into `dfs_helper`
        - Return list of visited nodes

- Helper function
    def dfs_helper(self, start_node, visited)
        - If `start_node` is not in list of visited nodes
            - Append `start_node` to list of visited nodes
            - Loop through `start_node`'s neighbors
                - Call dfs_helper passing in list of visited nodes and the neighbor
                  as the new start node
'''