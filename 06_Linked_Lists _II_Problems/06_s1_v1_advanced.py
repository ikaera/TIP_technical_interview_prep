# Week 6


'''
U - Understand
    I - Input - head of linked list (dna_strand), and two integers m and n
    O - Output - head of a modified linked list where the first m nodes are kept and the next n nodes are removed, and this pattern is repeated until the end of the list
    C - constraints/considerations - time complexity O(n), space complexity should be O(1)
    E - example/edge cases - 1 node in the linked list, m = 5 and n = 2. Return just the linked list?
    
P - Plan
    High-level: 
    var = m + n

    Steps: 
    1) init start pointer points to head
    2) while start;
        a) for m times
        keep first m elements moving start pointer m times
        if start become None, return the modified list
        b) for n times
        delete next n elements by moving another pointer 'temp'
        c) connect start node to node after n times deletion
        d) move 'start' to the next node 
    3) return head of modified node.       
h
            s
            t
1 2 3 4 5 6 7 8 9 10 11 12 13    
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
def edit_dna_sequence(dna_strand, m, n):
    start = dna_strand
    while start:
        for i in range(m - 1):
            if start is None: 
                return dna_strand
            start = start.next
        if start is None: 
            return dna_strand
        temp = start.next
        for j in range(n):
            if temp is None: 
                break
            temp=temp.next

        start.next = temp

        start = temp
    
    return dna_strand
# complexity space O(1), time O((N= (num of nodes) + (m-1) + n) = O(N)
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

# print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

'''    
U - Understand
    I - Input - head of linked list (protein)
    O - Output - Return an array with the values of any cycle in the list. 
    C - constraints/considerations
    E - example/edge cases - If there is no cycle, return null.
P - Plan
    High-level: 
    Using slow and fast pointers to detect a cycle. 
    Steps: 
    

I - Implement
'''

'''
'''