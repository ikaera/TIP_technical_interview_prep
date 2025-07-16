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
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def cycle_start(path_start):
	pass

# example usage
path_start = Node('Start', Node('Point 1', Node('Point 2', Node('Point 3'))))
path_start.next.next.next.next = path_start.next
print(cycle_start(path_start))

# Example Output:

# Point 1

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