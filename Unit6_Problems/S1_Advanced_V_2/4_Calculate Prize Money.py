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
        I - Input - the heads of two non-empty linked lists, prize_a and prize_b
        O - Output - revresed linked list representing the sum of the two numbers
        C - constraints/considerations
            the heads of two non-empty linked lists, prize_a and prize_b, representing two non-negative integers
        E - example/edge cases
    M - Match
    P - Plan
        High-level: 
        Steps:
        1. build integer from linked list a
        2. build integer from linked list b
        3. add the two integers then reverse the sum
        4. build a new linked list from the sum
        5. return the new linked list
    I - Implement
    '''
    current_a = head_a
    sum_a = 0
    while current_a:
        sum_a = sum_a * 10 + current_a.value
        current_a = current_a.next
        
    current_b = head_b
    sum_b = 0
    while current_b:
        sum_b = sum_b * 10 + current_b.value
        current_b = current_b.next

    total_sum = sum_a + sum_b
    # Reverse the total_sum and build a new linked list
    temp_head = Node(0)
    current = temp_head
    while total_sum:
        digit = total_sum % 10        
        new_node = Node(digit)  # Space complexity O(1)
        current.next = new_node
        current = current.next
        total_sum =  total_sum // 10
        # print(current.value)         
    return temp_head.next
# Example Usage:
# 342 and 465 and their sum 807 as linked lists with reversed digits

head_a = Node(2, Node(4, Node(3))) # 342  243
head_b = Node(5, Node(6, Node(4))) # 465  564

print_linked_list(add_two_numbers(head_a, head_b))
'''Example Output:

7 -> 0 -> 8
Explanation: 342 + 465 = 807 '''