''' Advanced Problem Set Version 1
Problem 1: Selective DNA Deletion
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. Each nucleotide in the sequence is represented as a node in the linked list, where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() that simulates the selective deletion of nucleotides in a DNA sequence. You will: - Start at the beginning of the DNA strand. - Retain the first 'm' nucleotides from the current position. - Remove the next 'n' nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.   
U - Understand
        I - Input - head of LL=dna_strand, int m, int n
        O - Output - the head of the modified DNA
        C - constraints/considerations
            - Retain the first 'm' nucleotides from the current position. 
            - Remove the next 'n' nucleotides from the sequence. - Repeat the process until the end of the DNA strand is reached.
        E - example/edge cases       

            edge cases
             - dna_strand LL has one node
             - dna_strand LL is Null
             - m and/or n are 0
    P - Plan
        High-level: 
            move both pointers m times, 
        Steps: 
            1. init 2 ptrs 'slow' and 'fast' 
                if LL is Null
            2. Loop thru the LL ('slow')
                1. move both ptrs to 'm-1' steps
                2. move the second ptr 'n+1'
                3. slow.next => fast
            3. if 
            4. return the head of the modified DNA  
    I - Implement'''
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
    slow = dna_strand
    fast = dna_strand
    while fast:
        count = 0
        for i in range(m-1):
            if slow is None or fast is None:
                return dna_strand
            slow = slow.next
            fast = fast.next
        for j in range(n+1):
            if fast is None:
                slow.next = None
                return dna_strand
            fast = fast.next
        slow.next = fast
# Example Usage:
dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

# print_linked_list(selective_trail_clearing(dna_strand, 2, 3))

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