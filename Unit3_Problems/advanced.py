# Advanced Problem Set Version 2
'''
Problem 1: Extra Treats
In a pet adoption center, there are two groups of volunteers: the "Cat Lovers" and the "Dog Lovers."

The center is deciding on which type of pet should be receive extra treats that week, and the voting takes place in a round-based procedure. In each round, each volunteer can exercise one of the two rights:

Ban one volunteer's vote: A volunteer can make another volunteer from the opposite group lose all their rights in this and all the following rounds.
Announce the victory: If a volunteer finds that all the remaining volunteers with the right to vote are from the same group, they can announce the victory for their group and prioritize their preferred pet for extra treats.
Given a string votes representing each volunteer's group affiliation. The character 'C' represents "Cat Lovers" and 'D' represents "Dog Lovers". The length of the given string represents the number of volunteers.

Predict which group will finally announce the victory and prioritize their preferred pet for extra treats. The output should be "Cat Lovers" or "Dog Lovers".
'''
'''
1. Initialize two queues, `cat_queue` and `dog_queue`, to hold the indices of the 'C' and 'D' volunteers, respectively.
2. Populate the queues with the positions of each 'C' and 'D' in the `votes` string.
3. Process the queues until one is empty:
   1. Compare the front positions of both queues.
   2. The volunteer whose position is earlier bans the other (i.e., removes them from the queue).
   3. The winner of this round re-enters the queue at a position that simulates moving to the end of the voting sequence (index + len(votes)).
4. If `cat_queue` is empty, return "Dog Lovers"; if `dog_queue` is empty, return "Cat Lovers".
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