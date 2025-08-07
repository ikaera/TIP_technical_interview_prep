from collections import deque
'''Problem 3: Finding All Reachable Destinations
You are a travel coordinator for CodePath Airlines, and you're helping a customer find all possible destinations they can reach from a starting airport. The flight connections between airports are represented as an adjacency dictionary flights, where each key is a destination, and the corresponding value is a list of other destinations that are reachable through a direct flight.

Given a starting location start, return a list of all destinations reachable from the start location either through a direct flight or connecting flights with layovers. The list should be provided in ascending order by number of layovers required.

    U - Understand
        I - Input: Given a starting location `start`
        O - Output: return a list of all destinations reachable from the start location either through a direct flight or connecting flights with layovers 
        C - constraints/considerations: The list should be provided in ascending order by number of layovers required.
        E - example/edge cases
            HAPPY CASE
            Input: 
            flights = {
                ""Tokyo"": [""Sydney""],
                ""Sydney"": [""Tokyo"", ""Beijing""],
                ""Beijing"": [""Mexico City"", ""Helsinki""],
                ""Helsinki"": [""Cairo"", ""New York""],
                ""Cairo"": [""Helsinki"", ""Reykjavik""],
                ""Reykjavik"": [""Cairo"", ""New York""],
                ""Mexico City"": [""Sydney""]
            }
            start = ""Beijing""
            Output: ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 'Reykjavik']
            Explanation: Starting from Beijing, you can reach all other destinations through direct and connecting flights.

            EDGE CASE
            Input: 
            flights = {
                ""Tokyo"": [""Sydney""],
                ""Sydney"": [""Tokyo""]
            }
            start = ""Tokyo""
            Output: ['Tokyo', 'Sydney']
            Explanation: Tokyo can only reach Sydney directly, and vice versa.
    Visited (DFS order):
        ['Beijing', 'Mexico City', 'Sydney', 'Tokyo', 'Helsinki', 'Cairo', 'Reykjavik', 'New York']
    Visited (BFS order):
        ['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 'Reykjavik']
    P - Plan
        High-level: BFS

        Steps: 
            - Initialize an empty list of visited nodes
            - Initialize an empty queue with starting city 'start'
            - init empty list 'reachable_dest' to store all cities that can be reached.
            - Add the node starting city 'start' we would like to start our traversal from to the queue 
            - Add the node we would like to start our traversal from to visited: start
            - While the queue is not empty:
                - Remove an element from the queue and store it in a variable, `current`
                - add current to `reachable_dest`
                - Loop through each of the current node's neighbors:
                    - If the neighbor has not yet been visited:
                        - Add the neighbor to the queue
                        - Add the neighbor to the list of visited nodes
            - Return the list list 'reachable_dest'

    I - Implement
'''
def get_all_destinations(flights, start):
    visited_nodes = set([start])
    queue = deque([start])
    reachable_dest = []
    while queue: 
        current = queue.popleft()
        reachable_dest.append(current) 
        for neighbor in flights.get(current, []):
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                visited_nodes.add(neighbor)

    return reachable_dest

# Example Usage:
flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
    "New York": []   
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
'''
Example Output:
['Beijing', 'Mexico City', 'Helsinki', 'Sydney', 'Cairo', 'New York', 'Tokyo', 
'Reykjavik']
['Helsinki', 'Cairo', 'New York', 'Reykjavik']
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