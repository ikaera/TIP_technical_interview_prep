# Week 3: Stacks, Queues, Two Pointer

# Problem Set Version 1

# Problem 1: Arrange Guest Arrival Order

def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    stack =[]
    result =[]

    for i in range(n+1):
        stack.append(i+1)

     #if at the end OR pattern says'I'
        if i == n or arrival_pattern[i] =='I':
            while stack:
                result.append(stack.pop())

    return ''.join(map(str, result))

     
#IIIDDD

#1234567
#STACK =[]
#RESUT =[]

#STACK = [4, 5, 6,7]
#RESULT =[1, 2, 3, 7,6,5,4]

# def arrange_guest_arrival_order(arrival_pattern):
#     n = len(arrival_pattern)
#     result = list(range(1, n + 2))
    
#     i = 0
#     while i < n:
#         if arrival_pattern[i] == 'D':
#             start = i
#             while i < n and arrival_pattern[i] == 'D':
#                 i += 1
#             result[start:i+1] = reversed(result[start:i+1])
#         else:
#             i += 1
    
#     return ''.join(map(str, result))
 
# Example Usage:
# print(arrange_guest_arrival_order("IIIDIDDD"))  # 123549876
# print(arrange_guest_arrival_order("DDD"))  # 4321

# Problem 2: Reveal Attendee List in Order
'''
You are planning a special event where each attendee has a unique registration number. These numbers are listed in the provided array attendees, but they are currently out of order.

At the event, attendees will walk on stage one by one following this special reveal process:

The person at the front of the line walks on stage (this number is revealed).
If there are still people left in line, the next person in front moves to the back of the line.
Steps 1 and 2 repeat until everyone has walked on stage.
Your task is to rearrange the attendees list before the process starts so that the attendees walk on stage by registration number in increasing order.

Write a function reveal_attendee_list_in_order(attendees) that returns an array with the correct starting order, such that when the attendees follow the above reveal process
they walk on stage from smallest registration number to largest registration number.
'''

'''
[2, 13, 3, 11, 5, 17, 7]

sort [ 2 3 5 7 11 13 17]

deque q = []

q is empty , so we append 17 -> q = [17]

next 13 : q is not empty, pop 17 and appendleft -> q = [17] then appendleft 13-> q = [13,17]


'''
'''

def reveal_attendee_list_in_order(attendees):

    return 0
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) #[2,13,3,11,5,17,7]
print(reveal_attendee_list_in_order([1,1000]))   # [1,1000]


# Problem 3: Arrange Event Attendees by Priority

# Problem 4: Rearrange Guests by Attendance and Absence

# Problem 5: Minimum Changes to Make Schedule Balanced

# Problem 6: Marking the Event Timeline

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
'''
