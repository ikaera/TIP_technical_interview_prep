# Week 7

'''
Problem 3: Find First and Last Frequency Positions

The Rebel Alliance has intercepted a crucial sequence of encrypted transmissions from the evil Empire. Each transmission is marked with a unique frequency code, represented as integers, and these codes are stored in a sorted array transmissions. As a skilled codebreaker for the Rebellion, write a function find_frequency_positions() that returns a tuple with the first and last indices of a specific frequency code target_code in transmissions. If target_code does not exist in transmissions, return (-1, -1).

Your solution must have O(log n) time complexity.
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
def find_frequency_positions(transmissions, target_code):
   
    def find_first(transmissions, target_code):
        left = 0
        right = len(transmissions) - 1
        first_p = -1
        while left <= right:
            midpoint = (left + right) // 2
            value = transmissions[midpoint]

            if value == target_code:
                first_p = midpoint
                right = midpoint - 1   # move LEFT
            elif value < target_code:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return first_p
        
    def find_last(transmissions, target_code):
        left = 0
        right = len(transmissions) - 1
        last_p = -1
        while left <= right:
            midpoint = (left + right) // 2
            value = transmissions[midpoint]

            if value == target_code:
                last_p = midpoint
                left = midpoint + 1   # move RIGHT
            elif value < target_code:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return last_p
    
    first_pos = find_first(transmissions, target_code)
    last_pos = find_last(transmissions, target_code)

    if first_pos != -1:
        return (first_pos, last_pos)
    else:
        return (-1, -1)
    
print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))
# Example Output:
(3, 4)
(-1, -1)
(-1, -1)
    
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

