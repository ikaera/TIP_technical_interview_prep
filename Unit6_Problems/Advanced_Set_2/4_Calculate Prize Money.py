"""Problem 4: Calculate Prize Money
In the game show, contestants win prize money for each of the challenges they participate in. Write a function get_total_prize() that accepts the heads of two non-empty linked lists, prize_a and prize_b, representing two non-negative integers. The digits are stored in reverse order and each node represents a single digit. The function should add the two numbers and return the sum of the prize money as a linked list.

The digits of the sum should also be stored in reverse order with each node containing a single digit.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity."""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def add_two_numbers(head_a, head_b):
    '''
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    M - Match
        P - Plan
        High-level: 

        Steps: 

    I - Implement
    '''
    pass

# Example Usage:
# 342 and 465 and their sum 807 as linked lists with reversed digits

head_a = Node(2, Node(4, Node(3))) # 342
head_b = Node(5, Node(6, Node(4))) # 465

print_linked_list(add_two_numbers(head_a, head_b))
'''Example Output:

7 -> 0 -> 8
Explanation: 342 + 465 = 807 '''