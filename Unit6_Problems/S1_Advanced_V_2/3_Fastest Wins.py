'''Problem 3: Fastest Wins!
Contestants, today's challenge is to sort a linked list of items the fastest! The catch - you have to follow a certain technique or you're disqualified from the round. You’ll start with an unsorted lineup, and with each step, you’ll move one item at a time into its proper position until the entire lineup is perfectly ordered.

Given the head of a linked list, sort the items using the following procedure:

Start with the first item: The sorted section initially contains just the first item. The rest of the items await their turn in the unsorted section.
Pick and Place: For each step, pick the next item from the unsorted section, find its correct spot in the sorted section, and place it there.
Repeat: Continue until all items are in the sorted section.
Return the head of the sorted linked list.

As a preview, here is a graphical example of the required technique (also known as the insertion sort algorithm). The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

Sorting unordered list of integers using insertion sort technique

When you have finished your sorting, receive bonus points for evaluating the time and space complexity of your solution. To get full points, you must define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
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

def sort_list(head):
	
    pass
# Example Usage:

# Example 1head1 list shown unsorted and sorted

# Example 2head1 list shown unsorted and sorted

head1 = Node(4, Node(2, Node(1, Node(3))))
head2 = Node(-1, Node(5, Node(3, Node(4, Node(0)))))

print_linked_list(sort_list(head1))
print_linked_list(sort_list(head2))

'''Example Output:

1 -> 2 -> 3 -> 4
-1 -> 0 -> 3 -> 4 -> 5
Hint: Temporary Head Technique
This problem may benefit from the temporary head technique. For reference, check out the unit cheatsheet.
'''