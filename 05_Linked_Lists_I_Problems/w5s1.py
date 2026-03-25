"""
Build a system that generates a valid quest completion order for an
RPG.

Input: 
    num_quests: total number of quests (0 to n - 1)
    prerequisites: a list of pairs where [a, b] means quest b must be
        finished before quest a

We'll show 2 ways to do this—DFS, then BFS.
"""

from collections import defaultdict, deque
from enum import Enum

"""
BFS solution:
    - Create an adj. list and mapping of how many prereqs each quest
        has remaining. Start with the quests with no prereqs, and
        decrement accordingly in the prereq count mapping for anything
        that requires it. If a quest no longer has any prereqs, add it
        to the queue to completed (added to the list). When the queue
        is empty, all quests are done, or there must be a cycle

Why this works:
    - If cycles exist, at some point the queue will be prematurely empty.
        Otherwise, quests will only be completed when no prereqs remain,
        so conceptually this is easier to understand than the DFS one.
        Another example of how BFS or DFS can be used to solve
        topological sort problems.

Conceptual algo:
    - create an adjacency list representing prereqs -> quests that require them
    - simultaneously, create a list/dict that represents how many prereqs each quest has before it can be completed
    - initialize a queue with all quests with no prereqs based on this ^ list
    - for each quest:
        - add it to our topological sort output list
        - subtract 1 from the requirement count for each node it points to (found in the adj list)
            - if a quest now has 0 remaining requirements, add it to the queue
    - repeat this process until the queue is empty
    - if the number of quests in our output list doesn't match the input num_quests, there must be a cycle
        - return an empty list
    - otherwise return the output list
"""
def quest_completion_order_bfs(num_quests: int, prerequisites: list[list[int]]) -> list[int]:
    # create adj list and prereq count map
    quest_deps = defaultdict(set)
    remaining_prereqs = [0] * num_quests
    for quest, prereq in prerequisites:
        quest_deps[prereq].add(quest)
        remaining_prereqs[quest] += 1
    
    # prepopulate queue with starter quests (quests with no prereqs)
    starter_quests = [i for i in range(num_quests) if remaining_prereqs[i] == 0]
    quest_queue = deque(starter_quests)
    quest_order = []
    while quest_queue:
        current_quest = quest_queue.popleft()
        quest_order.append(current_quest)
        if current_quest in quest_deps:
            # decrement the prereq count accordingly for quests that
            # have the current quest as a prereq
            for q in quest_deps[current_quest]:
                remaining_prereqs[q] -= 1
                # if there are no more prereqs for the given quest,
                # it can be completed — add it to the queue
                if remaining_prereqs[q] == 0:
                    quest_queue.append(q)
    # cycle check
    if len(quest_order) != num_quests:
        return []
    return quest_order

"""
DFS solution (similar to the one done in class):
    - Assemble the top. sort list in reverse order by digging through
        each path for the given problem. If you encounter any cycles,
        early return an empty list. Otherwise when the list if fully
        assembled (in reverse order), return the reversed version of that.

Why this works:
    - Handling quests with multiple dependencies can be tricky. By
        building the list in reverse order but starting with the
        prereqs, it naturally handles this case by always placing
        a prereq after the quest(s) that depend on it. Reversing this
        at the end keeps everything in valid order.

Conceptual algo:
    - create enums representing status
        - NOT_STARTED is not started yet
        - IN_PROGRESS is that quests it is a prereq for are also
            in-progress
        - FINISHED is completed, all quests that it is a prereq for are
            done
    - create the following
        - adj list (same as DFS) for each prereq -> quest
        - quest statuses list/dict
        - empty list representing quests completed in reverse order
    - for each quest, run the DFS recursive helper function. DFS does:
        - early return True is already finished
            - this handles nodes finished in an early DFS path
        - early return False if the node is already in-progress
            - this signals a cycle
        - mark the node as IN_PROGRESS
        - call DFS on all quests that depend on the current one
            - early return False if there is a cycle
        - mark the node as FINISHED and add it to the reverse-order list
        - return True
    - if at any point we returned False in DFS, return the empty list
    - otherwise return the output list but reversed
"""
class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 2

def quest_completion_order_dfs(num_quests: int, prerequisites: list[list[int]]) -> list[int]:
    post_order_quests = []
    # init all quests to NOT_STARTED and create adj list
    quest_visit_status = {i: Status.NOT_STARTED for i in range(num_quests)}
    quest_deps = defaultdict(list)
    for quest, prereq in prerequisites:
        quest_deps[prereq].append(quest)

    # recursive helper to process each quest
    def _dfs(quest: int) -> bool:
        if quest_visit_status[quest] == Status.FINISHED:
            return True
        if quest_visit_status[quest] == Status.IN_PROGRESS:
            # Cycle
            return False
        # mark the current quest as IN_PROGRESS so that if it's
        # re-encountered in this path, we know there is a cycle
        quest_visit_status[quest] = Status.IN_PROGRESS
        for q in quest_deps[quest]:
            # do it this way to early return for cycles (False)
            if not _dfs(q):
                return False
        # bubbled up from all _dfs calls, mark as finished and add this
        # quest to the output (in reverse order)
        quest_visit_status[quest] = Status.FINISHED
        post_order_quests.append(quest)
        return True
    
    # call _dfs on all quests
    # the FINISHED base case will early terminate for those already
    # finished in an earlier path
    for q in range(num_quests):
        # cycle detection -> just return the empty list
        if not _dfs(q):
            return []
        
    # reverse-order list is complete, just flip it to be a valid quest
    # order
    return post_order_quests[::-1]

# Simple example
prerequisites = [[2, 0], [3, 1], [3, 2]]
print(f"BFS: {quest_completion_order_bfs(4, prerequisites)}")
print(f"DFS: {quest_completion_order_dfs(4, prerequisites)}")
# Some more complicated examples
prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2], [4, 2], [5, 3], [5, 4]]
print(f"BFS: {quest_completion_order_bfs(6, prerequisites)}")
print(f"DFS: {quest_completion_order_dfs(6, prerequisites)}")

# Cycle example
prerequisites = [[1, 0], [2, 1], [0, 2]]
print(f"BFS: {quest_completion_order_bfs(3, prerequisites)}")
print(f"DFS: {quest_completion_order_dfs(3, prerequisites)}")
