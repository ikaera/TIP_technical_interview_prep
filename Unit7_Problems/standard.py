''' 
TIP102 Unit 7 Session 1 Standard
Raymond Chen edited this page on Aug 21, 2024 · 3 revisions
Part of TIP102 Unit 7

🔗 Problem Statements
Problem Set Version 1 (Solutions Only)
    Counting Iron Man's Suits
    Collecting Infinity Stones
    Counting Iron Man's Unique Suits
    Calculating Groot's Growth
    Calculating the Power of the Fantastic Four
    Strongest Avenger
    Counting Vibranium Deposits
    Merging Missions
    Merging Missions II

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
Problem Set Version 2 (Solutions Only)
    Calculating Village Size
    Counting the Castle Walls
    Reversing a Scroll
    Palindromic Name
    Doubling the Power of a Spell
    Checking the Knight's Path
    Finding the Longest Winning Streak
    Weaving Spells
    Weaving Spells II

Problem 2: Counting the Castle Walls
In a faraway kingdom, a castle is surrounded by multiple defensive walls, where each wall is nested within another. Given a list of lists walls where each list [] represents a wall, write a recursive function count_walls() that returns the total number of walls.

    U - Understand
        I - Input - a list of lists walls where each list [] represents a wall
        O - Output - total nums of walls
        C - constraints/considerations
        E - example/
        edge cases: 
        empty list of walls - The function should return 1, representing the outermost wall.
    P - Plan
        High-level: the number of walls can be counted by thining of each list as one wall, and recursivly counting each wall within it
        Steps: 
            Base cases: if list 'walls' is empty return 1
            Recursive case: return 1 (for the current wall) + recursive call on nested list 'walls[1]'

    I - Implement
'''
def count_walls(walls):
    # Base cases:
    if not walls: 
        return 1
    # Recursive case:
    return 1 + count_walls(walls[1])

# usage examples:
# HAPPY CASE
walls1 = ["outer", ["inner", ["keep", []]]]
# print(count_walls(walls1))
'''Output: 4
Explanation: The list represents four walls: "outer", "inner", "keep", and the empty list representing the innermost part.
'''
# EDGE CASE
walls0 =  []
# print(count_walls(walls0))
'''Output: 1
Explanation: Even an empty list represents a single wall, so the count is 1.
'''

'''
Problem 3: Reversing a Scroll
A wizard is deciphering an ancient scroll and needs to reverse the letters in a word to reveal a hidden message. Write a recursive function to reverse the letters in a given scroll and return the reversed scroll. Assume scroll only contains alphabetic characters.

    U - Understand
        I - Input - given scroll
        O - Output - the reversed scroll
        C - constraints/considerations - Assume scroll only contains alphabetic characters.
        E - example/
            HAPPY CASE
            Input: "cigam"
            Output: "magic"
            Explanation: The string "cigam" reversed is "magic".

            Input: "lleps"
            Output: "spell"
            Explanation: The string "lleps" reversed is "spell".

            EDGE CASE
            Input: "
            Output: "
            Explanation: An empty string should return an empty string.
            edge cases:
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
def reverse_scroll(scroll):
    if not len(scroll): 
        return scroll
    return reverse_scroll(scroll[1:]) + scroll[0]

# print(reverse_scroll("cigam")) # Output: "magic"
# print(reverse_scroll("lleps"))
# print(reverse_scroll(" "))
# print(reverse_scroll("abcd"))

'''
    U - Understand
        I - Input 
            a string comprised of only lowercase alphabetic characters 'name'
        O - Output - returns True if the name is palindromic and False otherwise.
        C - constraints/considerations - lowercase alphabetic characters 'name'
        E - example/edge cases
        
            HAPPY CASE
            Input: "eve"
            Output: True
            Explanation: The string "eve" reads the same forward and backward, so it is a palindrome.

            Input: "ling"
            Output: False
            Explanation: The string "ling" does not read the same forward and backward, so it is not a palindrome.

            EDGE CASE
            Input: "
            Output: True
            Explanation: An empty string is considered a palindrome by definition.

            Input: "a"
            Output: True
            Explanation: A single character string is always a palindrome.

    P - Plan
        High-level: 
        Steps: 
            Base case: 
            Recursive case: 

    I - Implement
'''
def is_palindrome(name):
    # Base case: if 'name' is empty or contins only one char, return true
    if len(name) <= 1:
        return True
    # Base case: if the first and last char does not match, return false 
    if name[0] != name[-1]:
        return False
    # Recursive case: call function recursivly passing input 'name' excluding the first and last char from it
    return is_palindrome(name[1:-1])

#edge cases
'''print(is_palindrome('e'))
print(is_palindrome(''))

print(is_palindrome('eve'))
print(is_palindrome('even'))
'''
'''
Problem 5: Doubling the Power of a Spell
The court magician is practicing a spell that doubles its power with each incantation. Given an integer initial_power and a non-negative integer n, write a recursive function that doubles initial_power n times.
U - Understand
    I - Input - Given an integer initial_power and a non-negative integer n, write a recursive function that doubles initial_power n times.
    O - Output  return doubled initial_power n times
    C - constraints/considerations
    E - example/ edge cases:
            HAPPY CASE
            Input: initial_power = 5, n = 3
            Output: 40
            Explanation: 5 doubled 3 times: 5 -> 10 -> 20 -> 40

            Input: initial_power = 7, n = 2
            Output: 28
            Explanation: 7 doubled 2 times: 7 -> 14 -> 28

            EDGE CASE
            Input: initial_power = 10, n = 0
            Output: 10
            Explanation: If no doubling is required, the initial power remains 10.
    
        edge cases: What should the function return if n is 0?
            The function should return the initial_power without any changes.
P - Plan
    High-level: 
    Steps: 
        Base case: if n is 0, return initial_power
        Recursive case: return func double_power passing doubled 'initial_power' and desrease n by 1 

I - Implement
'''
def double_power(initial_power, n):
    if n == 0:
        return initial_power
    # recursive case:
    return double_power(initial_power * 2, n - 1)

'''print(double_power(5, 3))
print(double_power(7, 2))
print(double_power(10, 0))
print(double_power(10, 1))
'''
'''
Problem 6: Checking the Knight's Path
A knight is traveling along a path marked by stones, and each stone has a number on it. The knight must check if the numbers on the stones form a strictly increasing sequence. Write a recursive function to determine if the sequence is strictly increasing.

U - Understand
    I - Input - list of int 'path'
    O - Output 
        if the sequence is strictly increasing return True | otherwise False
    C - constraints/considerations
    E - example/edge cases
            HAPPY CASE
        Input: [1, 2, 3, 4, 5]
        Output: True
        Explanation: The sequence 1 -> 2 -> 3 -> 4 -> 5 is strictly increasing.

        Input: [3, 5, 2, 8]
        Output: False
        Explanation: The sequence is not strictly increasing because 5 -> 2 decreases.

        EDGE CASE
        Input: []
        Output: True
        Explanation: An empty list is considered strictly increasing.

        Input: [7]
        Output: True
        Explanation: A single-element list is strictly increasing.
P - Plan
    High-level: 

    Steps: 
        1) Base case: If the list `path` is empty or has one element, return `True`.
        2) If the current element `path[0]` is greater than or equal to the next element `path[1]`, return `False`.
        3) Recursive case: Call the function on the rest of the list `path[1:]` and return the result.

I - Implement
'''
def is_increasing_path(path):
    if len(path) <= 1:
        return True
    if path[0] >= path[1]:
        return False
    # Recursive case:
    return is_increasing_path(path[1:])
# print(is_increasing_path([]))
# print(is_increasing_path([7]))
# print(is_increasing_path([1,2,3,4]))
# print(is_increasing_path([1,1,2,3]))

'''
Problem 7: Finding the Longest Winning Streak
In the kingdom's grand tournament, knights compete in a series of challenges. A knight's performance in the challenge is represented by a string challenges, where a success is represented by an S and each other outcome (like a draw or loss) is represented by an O. Write a recursive function to find the length of the longest consecutive streak of successful challenges (S).

U - Understand
    I - Input - 3 inputs: 
        string 'challenges', 
        int 'current_length'=0, 
        int 'max_length' wiht the default value of 0
    O - Output 'max_length'
    C - constraints/considerations
    E - example/edge cases
        HAPPY CASE
        Input: "SSOSSS"
        Output: 3
        Explanation: The longest streak of consecutive `S` is three, found at the end of the string.

        Input: "SOSOSOSO"
        Output: 1
        Explanation: The longest streak of consecutive `S` is only one.

        EDGE CASE
        Input: "
        Output: 0
        Explanation: An empty string has no challenges, so the longest streak is `0`.

        Input: "OOOOOO"
        Output: 0
        Explanation: There are no successful challenges, so the longest streak is `0`.
P - Plan
    High-level: 

    Steps: 

I - Implement
'''
def longest_streak(challenges, current_length=0, max_length=0):
    pass

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