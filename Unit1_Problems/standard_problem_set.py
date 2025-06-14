# U-nderstand
     # Understand what the interviewer is asking for 
     # by using test cases and questions about the problem.

# P-lan
    # Plan the solution with appropriate visualizations and pseudocode.

# I-mplement
    # Implement the code to solve the algorithm.

def linear_search(items, target):
    # Iterate thorugh the list
    # for i in range(len(items)):
        # check if the current el equals the target
    #     if items[i] == target:
    #         # print(i)
    #         return i            
    # return -1

    for i, item in enumerate(items):
        if item == target:
            return i    
    return -1
    
items = [ 'hunny', 'haycorn', 'haycorn', 'haycorn']
target = 'hunny'

# print(linear_search(items, target))

# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# initilize the tiger with value 1
# iterate though the list of operations
def final_value_after_operations(operations):
    tiger = 1
    for opt in operations:
    #   if opt == "bouncy" or opt == "flouncy": 
        if opt in ["bouncy", "flouncy"]:
            tiger+=1
        elif opt in ['trouncy', 'pouncy']:
            tiger-=1
    return tiger
# operations = ["trouncy", "flouncy", "flouncy"]
# operations = ["bouncy", "bouncy", "flouncy"]
# operations = []
# print(final_value_after_operations(operations))

def nanana_batman(x):    
    '''
    U - Understand
        I - Inputs
        O - Outputs
            None
        C - Constains/consideration
            - Cannot use the * to multiply "na"
            - When input is 0, be sure not to include the space
        E - Examples/edge cases
            Examples: 
                -  
            Edge case: 
                - Negative numbers ? -> return None
                - Zero -> 'batman'    
    P - Plan
            1) Using a loop, append 'na' to a string x times, 
                then append 'batman', then print the string
                Steps: 
                    1. Define the empty string result
                    2. Use a loop to concatenate "na" to the list x times
                    3. Append 'batman' to the result
                    4. Print the result
            2) Using a loop and a list, append "na" to the list x times, 
            then use ''.join() to merge the list, then append 'batman!'            
    '''
    if x== 0:
        print("batman!")
        return
    if x < 0:
        return None
    result = ""
    for _ in range(x):
        result += "na"
    result += " batman!"
    print(result)

# Test
'''nanana_batman(6)
print(nanana_batman(0))   # Should print: batman!
nanana_batman(3)   # Should print: nananana batman!
nanana_batman(-1)  # Should return: None'''

# Breakout Problems Session 2
# Standard Problem Set Version 1
"""
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.
"""
def reverse_sentence(sentence):
    pass
    """
    1. use split() to split sentence into words
    2. Reverse the list of words 
    3. using ''.join join the reversed the revesed list
    4. retun the resulting reversed sentence
    """
    words = sentence.split()
    reversed_words = words[::-1]
    result = " ".join(reversed_words)
    return result

# sentence = "tubby little cubby all stuffed with fluff"
# sentence = "Pooh"
# print(reverse_sentence(sentence))

# Problem 2: Goldilocks Number

'''
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.

Return the selected integer.

HAPPY CASES:
Input: [3, 2, 1, 4]
Expected Output: 2 or 3
Explanation: The minimum value is 1 and the maximum value is 4, so either 2 or 3 can be valid answers.

Input: [2, 1, 3]
Expected Output: 2
Explanation: Since 2 is neither the minimum nor the maximum value, it is the only valid answer.

EDGE CASES:
Input: [1, 2]
Expected Output: -1
Explanation: There is no number in nums that is neither the maximum nor the minimum, so no valid answer exists.

Input: [5]
Expected Output: -1
Explanation: Only one number exists in the list, so it cannot be neither the minimum nor the maximum.

General Idea: Check if the length of the list is less than or equal to 2. If so, return -1 since no valid number can exist. Identify the minimum and maximum values in the list. Iterate through the list and return the first number that is neither the minimum nor the maximum. If no such number is found, return -1.
'''

def goldilocks_approved(nums):
    if len(nums) <= 2:
        return -1
    for num in nums:
        if num != min(nums) or num != max(nums):
            return num
    return -1
# test:
nums = [3, 2, 1, 4]
# nums = [1, 2]
# nums = [2, 1, 3]
# nums = [5]
# print(goldilocks_approved(nums))

'''Problem 3: Delete Minimum
Pooh is eating all of his hunny jars in order of smallest to largest. Given a list of integers hunny_jar_sizes, write a function delete_minimum_elements() that continuously removes the minimum element until the list is empty. Return a new list of the elements of hunny_jar_sizes in the order in which they were removed.
HAPPY CASE
Input: [5, 3, 2, 4, 1]
Expected Output: [1, 2, 3, 4, 5]

Input: [5, 2, 1, 8, 2]
Expected Output: [1, 2, 2, 5, 8]

EDGE CASE
Input: [1, 1, 1, 1]
Expected Output: [1, 1, 1, 1]

Input: []
Expected Output: []
'''

def delete_minimum_elements(hunny_jar_sizes):
    result_list = []

    while hunny_jar_sizes:
        min_el = min(hunny_jar_sizes)
        result_list.append(min_el)
        hunny_jar_sizes.remove(min_el)
    return result_list
'''
    U - Understand
        I - Inputs
        O - Outputs
            None
        C - Constains/consideration            
        E - Examples/edge cases
            Examples:                 -  
            Edge case:    
    P - Plan
        1.
        2.
        3. Use a while loop to iterate as long as `hunny_jar_sizes` is not empty.
        4. Within the while loop:
            1. find the min element
            2. append this element to result_list
            3. remove the min element from hunny_jar_sizes
        5. return result_list

'''
# test: 
hunny_jar_sizes= [5, 3, 2, 4, 1]
# Expected Output: [1, 2, 3, 4, 5]

# hunny_jar_sizes= [5, 2, 1, 8, 2]
# Expected Output: [1, 2, 2, 5, 8]
print(delete_minimum_elements([5, 2, 1, 8, 2]))
# EDGE CASE
# hunny_jar_sizes= [1, 1, 1, 1]
# Expected Output: [1, 1, 1, 1]
print(delete_minimum_elements([1, 1, 1, 1]))
# hunny_jar_sizes= []
# Expected Output: []
print(delete_minimum_elements([]))
# print(delete_minimum_elements(hunny_jar_sizes))
