'''Problem 5: Next Contestant to Beat
You are given the head of a linked list contestant_scores with n nodes where each node represents the current score of a contestant in the game.

For each node in the list, find the value of the contestant with the next highest score. That is, for each score, find the value of the first node that is next to it and has a strictly larger value than it.

Return an integer array answer where answer[i] is the value of the next greater node of the ith node (1-indexed). If the ith node does not have a next greater node, set answer[i] = 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

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

def next_highest_scoring_contestant(contestant_scores):
    pass
'''Example Usage:

Example 1Linked List contestant_scores1 with dotted arrows to next greatest node

Example 2Linked List contestant_scores2 with dotted arrows to next greatest node
'''
contestant_scores1 = Node(2, Node(1, Node(5)))
contestant_scores2 = Node(2, Node(7, Node(4, Node(3, Node(5)))))

print(next_highest_scoring_contestant(contestant_scores1))
print(next_highest_scoring_contestant(contestant_scores2))
'''Example Output:

[5, 5, 0]
[7, 0, 5, 5, 0]
💡 Hint: Blast from the Past!
To solve this problem, you may find it helpful to use a data structure we learned about in Unit 3: a stack!'''