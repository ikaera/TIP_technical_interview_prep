"""Problem 2: Cycle Start
On your marks, get set, go! Contestants in the game show are racing along a path that contains a loop, but there's a hidden mini challenge: they aren't told where along the path the loop begins. Given the head of a linked list, path_start where each node represents a point in the path, return the value of the node at the start of the loop. If no loop exists in the path, return None.

A linked list has a cycle or loop if at some point in the list, the node’s next pointer points back to a previous node in the list.
   
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
"""
# Problem 2: Cycle Start
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
    slow , fast = path_start, path_start
    is_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            is_cycle = True
            break
    # if no cycle is detected, return None
    if not is_cycle:
        return None
    # Phase 2: Find the start of the cycle
    slow = path_start # reset slow pointer to the start of the path=head
    while is_cycle and slow != fast: # while loop will continue until slow and fast meet again
        slow = slow.next # move slow pointer one step
        fast = fast.next # move fast pointer one step
        
    return slow.value # meeting point === the start of the cycle

# example usage
path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))

# Example Output:
# Point 1
'''Test Case 1: Cycle at the Second Node
Linked List: A -> B -> C -> B (cycle starts at B)
Expected Output: B
Explanation:

Phase 1: slow and fast meet at C.

Phase 2: After reset, they meet again at B (cycle start).'''
# Setup
n1 = Node('A')
n2 = Node('B')
n3 = Node('C')
n1.next = n2
n2.next = n3
n3.next = n2  # Cycle: B -> C -> B

print(cycle_start(n1))  # Output: 'B'

'''Test Case 2: Single-Node Cycle
Linked List: A -> A (cycle starts at A)
Expected Output: A
Explanation:

Phase 1: slow and fast meet immediately at A.

Phase 2: Already at the cycle start.'''
n1 = Node('A')
n1.next = n1  # Cycle: A -> A
print(cycle_start(n1))  # Output: 'A'

'''Test Case 3: No Cycle (Linear List)
Linked List: A -> B -> C -> D (no cycle)
Expected Output: None
Explanation:
Phase 1: fast reaches the end (None) without meeting slow.'''
n1 = Node('A')
n2 = Node('B')  
n3 = Node('C')
n1.next = n2
n2.next = n3
n3.next = None
print(cycle_start(n1))  # Output: None

'''
✨ AI Hint: Slow and Fast Pointers
Key Skill: Use AI to explain code concepts

This problem requires a variation of the two-pointer technique called the slow and fast pointer technique! For reference, check out the Unit 5 Cheatsheet.

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the slow and fast pointer technique.

✨ AI Hint: Multiple Pass Technique
Key Skill: Use AI to explain code concepts

This problem may require multiple traversals of the list. For reference, check out the Unit 6 Cheatsheet.

For more help, you can use an AI tool like ChatGPT or GitHub Copilot to show you examples of the multiple pass technique.
'''