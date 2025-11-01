''' Week 5
Breakout Problems Session 2
Standard Problem Set Version 1
Problem 1: Mutual Friends
U - Understand
    I - Input
        one parameter, a Villager instance new_contact
    O - Output 
        returns a list with the name of all friends the current villager and new_contact have in common.
    C - constraints/considerations
    E - example/edge cases
        no mutual friends return empty.
P - Plan
    High-level: 

    Steps: 
    1. Init list result
    2. Loop though the the friends  

I - Implement

'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        result = []
        for friend in self.friends:
            if friend in new_contact.friends:
                result.append(friend.name)
        return result
# time and space O(n)
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))
'''
U - Understand

    I - Input
        head
    O - Output         
        prints the values of the list has also been provided for testing purposes
    C - constraints/considerations
    E - example/edge cases
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# Add code here to link the above nodes
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# print_linked_list(kk_slider)

'''
Problem 3: Daily Tasks
U - Understand
    I - Input
        head
    O - Output         
        prints the values of the list has also been provided for testing purposes
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
Standard Problem Set Version 1
Problem 1: New Horizons
U	Understand problem fully (I-O-C-E)
    Goal: build complete clarity on what problem you’re solving.
M	Match to known patterns or algorithms
    Purpose: Rather than starting from scratch, see if the problem resembles something you already know, which saves time and leads to better solutions.
P	Plan approach and data structures
    Purpose: To have a roadmap so that when you write code, you’re less likely to get lost.
I	Implement code based on plan
    Purpose: Turn your idea into something that runs.
R	Review code for correctness and clarity
    Purpose: To catch mistakes before running.
E	Evaluate performance, run tests, and think about improvements
    Purpose: Validate correctness and efficiency.

    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 

    I - Implement
# '''
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []

# # Instantiate your villager here
# 
# print(apollo.name)  
# print(apollo.species)  
# print(apollo.catchphrase) 
# print(apollo.furniture) 

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

Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:
'''
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.furniture = []
#     def greet_player(self, player_name):
#         return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

# apollo = Villager('Apollo', 'Eagle', 'pah')
# bones = Villager('Bones', 'Dog', 'yip yip')

# # Step 3: Call the method greet_player() with your name and print out
# name = "Zernima"
# bones.catchphrase = 'ruff it up'

# print(bones.greet_player("Samia"))


'''
Problem 4: Set Character
In the previous exercise, we accessed and modified a player’s catchphrase attribute directly. Instead of allowing users to update their player directly, it is common to create setter methods that users can call to update class attributes. This has a few different benefits, including allowing us to validate data before updating our class instance.

Update your Villager class with a method set_catchphrase() that takes in one parameter new_catchphrase.

If new_catchphrase is valid, it should update the villager's catchphrase attribute to have value new_catchphrase and print "Catchphrase updated".
Otherwise, it should print out "Invalid catchphrase".
Valid catchphrases are less than 20 characters in length. They must all contain only alphabetic and whitespace characters.
'''
import re as re
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []        
    def set_catchphrase(self, new_catchphrase):
        l = len(new_catchphrase)
        def is_alpha_or_whitespace(s):
            return bool(re.match(r'^[A-Za-z\s]+$', s))
        if l < 20:  
            
            if is_alpha_or_whitespace(new_catchphrase):
                self.catchphrase = new_catchphrase
                print("Catchphrase updated")
        else: 
            print("Invalid catchphrase")         

# alice = Villager("Alice", "Koala", "guvnor")

# alice.set_catchphrase("sweet dreams")
# print(alice.catchphrase)
# alice.set_catchphrase("#?!")
# print(alice.catchphrase)      
    
# class Node: 
#     def __init__(self, value):
#         self.value = value
#         self.next = None
        
# x = Node(2)
# y = Node(4)
# x.next = y
# y = None
# print (x.value)
# print()

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
P - Plan
    Goal: find the middle node (second middle if even length)
    High-level: use slow and fast pointers
    Steps: 
        1. Init 2 pointers: 'slow' and 'fast'; start both at the head
        2. Move 'fast' by 2 steps each time, and 'slow' by 1 step 
        3. Repeat until 'fast' reaches the end
        4. at that point 'slow' is pointing to: 
            1. the middle node if list len is odd
            2. the second middle node if list len is even
        5. Return 'slow' (node itself not just value) 
    Complexity: 
        O(n) time and O(1) space
'''
class Node:
    def __init__(self, val, next=None):
        self.value = val
        self.next = next

def middleNode(head):
    # init 'slow' and 'fast' ptrs
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

# Test Case 1: Odd-Length List (e.g., [1, 2, 3, 4, 5])
node5 = Node(5)
node4 = Node(4, node5)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

middle = middleNode(node1)
# print(middle.value)  # Should print 3

# Test Case 2: Even-Length List (e.g., [1, 2, 3, 4])
# Construct list: 1 -> 2 -> 3 -> 4
node4 = Node(4)
node3 = Node(3, node4)
node2 = Node(2, node3)
node1 = Node(1, node2)

middle_node =  middleNode(node1)
# print(middle_node.value)
'''
**Breakout Problems Session 2**
*Standard Problem Set Version 1*
Problem 1: Mutual Friends
In the Villager class below, each villager has a friends attribute, which is a list of other villagers they are friends with.

Write a method get_mutuals() that takes one parameter, a Villager instance new_contact, and returns a list with the name of all friends the current villager and new_contact have in common.
    U - Understand
        I - Input 
            new_contact
        O - Output 
             a list wiht the 'name'
        C - constraints/considerations            
        E - example/edge cases
            when there is no mutual friend we return an empty list
    P - Plan
        High-level: loop thru the friends list of an instance and chekc if the are in the friends list of the 'new_contact'

        Steps: 
            1. define an empty list 'result'
            2. Loop thru the friends list
                1. at each iteration, if friend of villiger is in the friends list of the 'new_contact'
                2. if friend is found in both lists, then add their names to the result
            3. Return the result list
    I - Implement
'''
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        result = []
        for f in self.friends:
            if f in new_contact.friends:
                result.append(f.name)
        return result
# 
# Example Usage:
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))

"""
Problem 2: Linked Up
A linked list is a data structure that, similar to a normal list or array, allows us to store pieces of data sequentially. The key difference is how the elements are stored in memory.

In a normal list, elements are stored in adjacent memory locations. If we know the location of the first element, we can easily access any other element in the list.

In a linked list, individual elements, called nodes, are not stored in sequential memory locations. Instead, each node stores a reference or pointer to the next node in the list, allowing us to traverse the list.

Connect the provided node instances below to create the linked list 
kk_slider -> harriet -> saharah -> isabelle.

A function print_linked_list() which accepts the head, or first element, of a linked list and prints the values of the list has also been provided for testing purposes.
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 
        1. link 'kk_slider.next' -> harriet 
        2. link 'harriet.next' -> saharah 
        3. link 'saharah.next' -> isabelle
    I - Implement
"""
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

kk_slider = Node("K.K. Slider")
harriet = Node("Harriet")
saharah = Node("Saharah")
isabelle = Node("Isabelle")

# link nodes: kk_slider -> harriet -> saharah -> isabelle
kk_slider.next = harriet
harriet.next = saharah
saharah.next = isabelle

# Test
# print_linked_list(kk_slider)
'''

Problem 3: Daily Tasks
Imagine a linked list used as a daily task list where each node represents a task. Write a function add_task() that takes in the head of a linked list and adds a new node to the front of the task list.

The function should insert a new Node object with the value task as the new head of the linked list and return the new node.

Note: The "head" of a linked list is the first element in the linked list. It is equivalent to lst[0] of a normal list.
U - Understand
        I - Input 
            head and task
        O - Output 
            new_node
        C - constraints/considerations
            Note: The "head" of a linked list is the first element in the linked list. 
            It is equivalent to lst[0] of a normal list.
        E - example/edge cases
            Example Usage:
                task_1 = Node("shake tree")
                task_2 = Node("dig fossils")
                task_3 = Node("catch bugs")
                task_1.next = task_2
                task_2.next = task_3
            edge cases:
                if task list is empty new_node will have only one node
    P - Plan
        High-level: Insert a new node at the beginning of the ll and make it the new head
        Steps: 
        1. Init a 'new_node' with the given task 
        2. insert a new Node object 'new_node' with the value task as the new head of the linked list, 
            point the new_nodes.next to the current head
        3. return the new node.
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
def add_task(head, task):
    new_node = Node(task)
    new_node.next = head
    head = new_node
    return new_node    

# # Example Usage:
# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_task(task_1, "check turnip prices"))

# # Test adding to an empty list
# head = None
# head = add_task(head, "water flowers")
# print_linked_list(head)  # Expected: water flowers

# # Test adding to a single-node list
# head = Node("sell items")
# head = add_task(head, "buy tools")
# print_linked_list(head)  # Expected: buy tools -> sell items

# # Test adding empty string
# head = Node("valid task")
# head = add_task(head, "")
# print_linked_list(head)  # Expected:  -> valid task

# # Test adding None
# head = Node("valid task")
# head = add_task(head, None)
# print_linked_list(head)  # Expected: None -> valid task

# # Verify original head is correctly preserved in the next pointer
# original_head = Node("original")
# new_head = add_task(original_head, "new")
# print(new_head.next is original_head)  # Expected: True

# # Test chained operations
# head = add_task(add_task(add_task(None, "third"), "second"), "first")
# print_linked_list(head)  # Expected: first -> second -> third

'''
Problem 4: Halve List
Write a function halve_list() that accepts the head of a linked list whose values are integers and divides each value by two. Return the head of the modified list.
    U
    M
    P - plan:
            steps: 
                1. Create 'current' and point to head
                2. Iterate thru ll
                    1. divides each value by two
                    2. move 'current' pointer to the next node
                3. Return the head of the modified list.
    I
    R
    E
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        # current.value = current.value / 2
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def halve_list(head):
    current = head
    while current: # O(n) time
        current.value = current.value / 2
        current = current.next
    return head    
# Example Usage:

node_one = Node(5)
node_two = Node(6)
node_three = Node(7)
node_one.next = node_two
node_two.next = node_three

# Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

'''Linked Lists II
Standard Problem Set Version 1
Problem 1: Building a Playlist
U - Understand
    I - Input - NO
    O - Output  - NO
    C - constraints/considerations - 
    E - example/edge cases
        ll is empty 
P - Plan
    High-level: 

    Steps: 

I - Implement
'''
class SongNode:
    def __init__(self, song, next=None):
        self.song = song
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print(current.song, end=" -> " if current.next else "")
        current = current.next
    print()
        
# top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Bad Romance")))
bad_romance = SongNode("Bad Romance")
party_rock_anthem = SongNode("Party Rock Anthem", bad_romance)
top_hits_2010s = SongNode("Uptown Funk", party_rock_anthem)

# print_linked_list(top_hits_2010s)


'''
Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
U - Understand
    I - Input - head of the ll
    O - Output - dictionary mapping each artist in the list to its frequency 
    C - constraints/considerations
    E - example/edge cases
P - Plan
    High-level: 
    Steps: 
        - create a dictionary 'result'
        - traverse the ll 
            - 

I - Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    results = {}
    current = playlist
    while current:
        if current.artist in results:
            results[current.artist] +=1
        else:
            results[current.artist] = 1
        current = current.next
    
    return results
# complexity time: O(n) and space: O(n)
# Example Usage:
playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

# print(get_artist_frequency(playlist))

# Example Output:
# { "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}


'''Problem 3: Glitching Out
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
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next        
# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()
# Function with a bug!
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    if playlist_head.song == song:
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song == song:
            current.next = current.next.next  
            return playlist_head 
        current = current.next
    return playlist_head
# complexity time: O(n) and space: O(1)

# Example Usage:
playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))

# Expected Output:
# ('SOS', 'ABBA') -> ('Simple Twist of Fate', 'Bob Dylan') -> ('Lovely Day', 'Bill Withers')

'''Problem 4: On Repeat

U - Understand
    I - Input
    O - Output 
    C - constraints/considerations
    E - example/edge cases
P - Plan
    High-level: 

    Steps: 
    - slow and fast
        - slow will go one step ahead and

I - Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

def on_repeat(playlist_head):
    pass

'''
Standard Problem Set Version 1
Problem 2: Breaking the Cycle
U - Understand
    I - Input - head of the ll
    O - Output - returns an array containing all values that are part of any cycle in evidence. 
    C - constraints/considerations - Return the values in any order.
    E - example/edge cases:
        - empty ll, 
        - only 1 node
P - Plan
    High-level: 
    Steps:         
        Detect cycle: 
        - if not 'evidence' return False
        - slow and fast ptr => evidence (head)
        - while (fast and fast.next):
            - slow moves 1 step ahead
            - fast moves 2 steps ahead
            - If they meet, there's a cycle
        fast == slow are the end of the cycle
        Find the start of the array:
        we can reset slow to head or evidence
        - while :
            slow 1 step ahead
            fast 1 step ahead
        Append the array
        start = slow
        temp = start
        init result_array
        while:
            append temp. values to the result_array
            move temp one step a time
        return result_array
I - Implement
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if not evidence:
        return False        
    slow = fast = evidence
    # 1
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow != fast: 
            return []
        else: 
            break
    # 2
    slow = evidence
    while slow != fast:
        slow = slow.next
        fast = fast.next
    #3
    start = slow
    result_array = []
    tmp = start
    while True:
        result_array.append(tmp.value)
        tmp = tmp.next
        if tmp == start:
            break
    return result_array

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

# print(collect_false_evidence(clue1))
# print(collect_false_evidence(clue5))
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
