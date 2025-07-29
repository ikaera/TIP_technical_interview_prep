"""
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.

"""
def is_valid_post_format(posts):
    result_stack = []
    tags_set = {'()', '[]', '{}' }
    if not posts:
       return False
    for c in posts:
        if c  == '(' or c == '[' or c == '{':
          result_stack.append(c)
        elif c  == ')' or c == ']' or c == '}':
          if not result_stack:
             return False
          elif (result_stack.pop() + c not in tags_set): 
            return False
    return not result_stack

''' 
Understand: 
    Input: string 'posts'
    Iutput boolean 
    Edge cases: empty string, start with ')', ']'  '}'
    Example: 
Plan: 
   1) Handle edge cases
   2) build an empty stack 
   3) loop though the posts
        if it is opening tag, add to the stack. 
        if it is closing tag,then check:
            if stack it empty return false
            if stack contains at the top different kind of opening tag
            if tag matches, pop the opening tag
        We continue this throgh the entire sting             
   4) check the stack: 
    '''   
    
'''
#   Example Usage: '''
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}")) 
# print(is_valid_post_format("(]"))
# print(is_valid_post_format(""))


'''
Problem 2: Reverse User Comments Queue
On your platform, comments on posts are displayed in the order they are received. However, for a special feature, you need to reverse the order of comments before displaying them. Given a queue of comments represented as a list of strings, reverse the order using a stack.

Undersand: 
    Input: comments
    Outputs: list 
Plan: 
    1) init stack
    2) loop each comment: 
        push to the stack
    3) init result_list
    4)pop elements from the stack
'''


def reverse_comments_queue(comments):
    stack = []
    for c in comments: 
       stack.append(c)

    results = []
    while stack:
        result = stack.pop()
        results.append(result)
    return results

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# *Standard Problem Set Version 2*
"""
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string, use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.

"""

'''
    U - Understand the problem
        I - Input = a post title as a string named 'title'
        O - Output = boolean,  
        C - constraints/considerations - 
            - ignoring spaces, 
            - punctuation, and case.    
        E - example/edge cases
            - title is empty or 
            - contains only non-alphanumeric characters
    P - Plan a step by step sol
        High-level: 
            use a new algorithmic technique the two-pointer method to compare 
            each char of the entire title string: 
            one pointer pointing to the first char and moving towards right and 
            the other char pointing to the last char and moving towards left 
                while ignoring spaces, punctuation,(non-alphanumeric characters) and case. 
        Steps: 
        1. init 2 pointers, 'left' at the start of tile and 'right' at the end
        2.  while 'left' is < 'right'
            1. while current char at 'left' index is non-alphanumeric char 
                 move 'left' pointer to the right
            2. while current title char at 'right' index is non-alphanumeric
                move right pointer to the left 
            3. convert char at 'left' and char at 'right' to lowercase and compare them: 
                1. if they do not match return False right away
                2. if they match move, move both p-s toward each other
        3. return True
    I - Implement
'''
import re
def is_symmetrical_title(title):
    left_p = 0
    right_p = len(title) - 1
    while left_p < right_p:
        # ignoring spaces, punctuation from the right
        while left_p<right_p and not title[right_p].isalnum():  # or bool(re.search(r'[^a-zA-Z0-9]', title))
            right_p -=1 
        while left_p < right_p and bool(re.search(r'[^a-zA-Z0-9]', title[left_p])):
            left_p +=1
        # compare chars (case-insensitive) 
        if title[left_p].lower() != title[right_p].lower():
           return False  
       
        left_p  +=1
        right_p -=1
    return True 

# Example Usage:
# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 
# print(is_symmetrical_title("%$# a Santa at NASA!!!!!"))


'''

Problem 4: Engagement Boost
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
'''
def engagement_boost(engagements):
    # init an empty list 
    squared_engagements = []
    # square each engagement value, pair it with original index and 
    # append to the list as tuple 
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        # Store the squared value along with its original index as a tuple
        squared_engagements.append((squared_engagement, i))
    # sort 'squared_engagements' in descending order (highest to lowest)
    squared_engagements.sort(reverse=True)
    # Initialize a result list with zeros, having the same length as the input
    result = [0] * len(engagements)
    # start position pointer at the end of the 'result' list (will move towards left) 
    position = len(engagements) - 1
    # loop thru 'squared_engagements'
    for square, original_index in squared_engagements:
        # place the current squared value at the current position
        result[position] = square
        # move the position pointer one step towards left
        position -= 1
    # return the final 'result' list containing squared values arranged in ascending order
    return result

# Example Usage:
'''print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
print(engagement_boost([-7, -3, 2, -3, -11]))
'''
'''
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 
            use 2 pt technique to efficiently compute the squares of the engagement rates
              and sort them ascending order   
        Steps: 
            1. init 2 pts, 'left' (at start) and 'right' (at the end)
            2. init 'results' list
            3. loop thru the list from the end towards the beginning:
                1. Compare the square of the value at `left` with the square of the value at `right`.
                2. Place the larger square at the current position in the result list.
                3. Move the corresponding pointer inward (left or right) based on which square was larger.
                4. Decrement the position in the result list.
            4. Return the result list, which contains the squared engagements in sorted order.
    I - Implement
'''
def engagement_boost_2pt(engagements):
    left_p = 0
    right_p = len(engagements) - 1
    results_list = [0] * len(engagements)
    # start position pointer at the end of the 'result' list (will move towards left) 
    position = len(engagements) - 1

    while left_p <= right_p:
        left_sq = engagements[left_p] ** 2
        right_sq = engagements[right_p] **2
        if right_sq > left_sq:
            results_list[position] = right_sq
            right_p -= 1
        else: 
            results_list[position] = left_sq
            left_p += 1
        # print(results_list)
        position -= 1
    return results_list

# Example Usage:
print(engagement_boost_2pt([-4, -1, 0, 3, 10]))
print(engagement_boost_2pt([-7, -3, 2, 3, 11]))
print(engagement_boost_2pt([-20, -10, -7, -3, 2, 3, 11, 20]))

'''Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]       
'''
