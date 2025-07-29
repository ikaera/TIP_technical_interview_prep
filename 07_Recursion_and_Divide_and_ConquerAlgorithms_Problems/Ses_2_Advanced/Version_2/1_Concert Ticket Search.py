'''
Advanced Problem Set Version 2
Problem 1: Concert Ticket Search
You are helping a friend find a concert ticket they can afford in a sorted list ticket_prices. Return the index of the ticket with a price closest to, but not greater than their budget.

Your solution must have O(log n) time complexity.

U - Understand
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/edge cases
M - Match
P - Plan
    High-level: 

    Steps: 

I - Implement '''
def find_affordable_ticket(prices, budget):
    left, right = 0, len(prices) - 1
    res = -1  

    while left <= right:
        mid = (left + right) // 2
        if prices[mid] <= budget:
            res = mid
            left = mid + 1
        else:
            right = mid - 1

    return res
# print(find_affordable_ticket([50, 75, 100, 150], 90))
# # Example Usage:

# print(find_affordable_ticket([50, 75, 100, 150], 90))
# Example Output:

'''1
Explantion: 75 is the closest ticket price less than or equal to 90. 
It has index 1. 
'''
# recursive 
"""
U 
    Input - list 'prices' and int budget
    Output - 
        the index of the ticket with a price closest   to, but not greater than their budget
    Constraints:
    Edge cases:
        base case: 
Match: Recursion

P - Plan:
    Steps: 
        1. Def the helper function  binary_search
        2. init result = -1
        3. Base case: if left > right, return -1
        3. calc 'mid' = (left + right) // 2
        4. if prices at mid = budget return 'mid'
        5. if prices at mid < budget, 
            result = mid
            recursive call 'binary_search' mid + 1 and right, 
        6. if prices at mid > budget return left, mid - 1
        7. return result
"""
def find_affordable_ticket(prices, budget):
    
    # helper function
    def binary_search(left, right):
        result = -1
        # Base case
        if left > right: 
            return -1
        mid = (left + right) // 2

        if prices[mid] == budget:
            return mid
        if prices[mid] < budget:
            result = mid
            binary_search(mid + 1, right)        
        if prices[mid] > budget:
            binary_search(left, mid - 1)
    binary_search()
# Example Usage:

print(find_affordable_ticket([50, 75, 100, 150], 90))
'''Example Output:

2 
Explantion: 75 is the closest ticket price less than or equal to 90. 
It has index 2. 
'''

'''
Problem 1: Counting the Layers of a Sandwich
You're working at a deli, and need to count the layers of a sandwich to make sure you made the order correctly. Each layer is represented by a nested list. Given a list of lists sandwich where each list [] represents a sandwich layer, write a recursive function count_layers() that returns the total number of sandwich layers.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

U - Understand
    I - Input
        a list of lists sandwich where each list [] represents a sandwich layer
    O - Output 
        returns the total number of sandwich layers
    C - constraints/considerations
    E - example/edge cases
M - Match
P - Plan
    High-level: 

    Steps: 

I - Implement '''
def count_layers(sandwich):
    pass
# Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))
'''Example Output:

4
5

'''
