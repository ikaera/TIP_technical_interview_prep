"""
Breakout Problems Session 1
    Standard Problem Set Version 1
        Problem 1: Building a Playlist
        The assignment statement to the top_hits_2010s variable below creates the linked list Uptown Funk -> Party Rock Anthem -> Bad Romance. Break apart the assignment statement into multiple lines with one call to the Node constructor per line to recreate the list.
"""
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
''' P - plan 
        steps: 
            1. create the last node 
            2. create the second to the last node and link it ot he last node and etc... (move backward to the first node)
            3. the first node will serve as the head of LL
'''
node_last = SongNode('Bad Romance')
node2 =  SongNode("Party Rock Anthem", node_last )
top_hits_2010s = SongNode("Uptown Funk", node2) 
# Example Usage:
# print_linked_list(top_hits_2010s)

'''
HAPPY CASE
Input: top_hits_2010s = SongNode("Uptown Funk", SongNode("Party Rock Anthem", SongNode("Telephone")))
Output: Uptown Funk -> Party Rock Anthem -> Telephone
Explanation: The output is the linked list where each node points to the next in sequence.

EDGE CASE
Input: top_hits_2010s = None
Output: (no output)
Explanation: An empty list (no nodes) should simply print nothing.
'''
third_node = SongNode("Telephone", None)
second_node = SongNode("Party Rock Anthem", third_node)
top_hits = SongNode("Uptown Funk", second_node)

# print_linked_list(top_hits)

''' 
Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.   
    U - Understand
        I - Input - the head of a linked list 'playlist', that is an instanc of 'SongNode'
        O - Output 
            a dictionary that maps each artist in the list to its frequency.
        C - constraints/considerations
        E - example/edge cases
            HAPPY CASE
                Input: playlist = SongNode("Saturn", "SZA", SongNode("Who", "Jimin", SongNode("Espresso", "Sabrina Carpenter", SongNode("Snooze", "SZA"))))
                Output: {"SZA": 2, "Jimin": 1, "Sabrina Carpenter": 1}
                Explanation: The artist "SZA" appears twice, while "Jimin" and "Sabrina Carpenter" appear once.

            EDGE CASE
                Input: playlist = None
                Output: {}
                Explanation: An empty linked list should return an empty dictionary.
    M - Match
            - Traversing the LL
            - Using a dict
    P - Plan
        High-level: traverse the LL and for each artist upadte the frequency cound in a dict
        Steps: 
            1. Inint an empty dict 'result' and 
            'current' pointing to head of 'playlist'
            2. Using a loop Traverse the LL staring from 'head'
                1. for each node at each iteration, check if the artist is in dict
                    a) If the artist is present, increment the frequency count.
                    b) else: If the artist is not present, add it to the dictionary with a frequency count of 1.
                2. continue untill the end of LL ('current' is True)
            3. return 'result' dict         
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
    result = {}
    current = playlist
    while current: 
        if current.artist not in result:
            result[current.artist] = 1
        else: 
            result[current.artist] += 1        
        current = current.next
    return result

# Example Usage:
# playlist = None
# print(get_artist_frequency(playlist))
"""
Problem 3: Glitching Out
"""
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


# Function with a bug fixed! 
def remove_song(playlist_head, song):
    if not playlist_head:
        return None
    # If the head node itself needs to be removed
    if playlist_head.song.upper() == song.upper():
        return playlist_head.next

    current = playlist_head
    while current.next:
        if current.next.song.lower() == song.lower():
            '''
            print(f'current.song is: {current.song}')
            print(f'current.next.song is: {current.next.song}')
            print(f'current.next.next.song is: {current.next.next.song}')'''
            # FIX: properly update the next pointer to skip the node
            current.next = current.next.next 
            '''Why the Alternative is Wrong:
                - 'current' = 'current.next.next' only changes the local variable 'current' to point two nodes ahead
                - It doesn't actually modify the linked list structure - the nodes remain connected as they were
                -The node we wanted to remove would still be part of the list'''
        
            return playlist_head 
        current = current.next

    return playlist_head

# Example Usage: 
playlist = SongNode("SOS", "ABBA", 
                SongNode("Simple Twist of Fate", "Bob Dylan",
                    SongNode("Dreams", "Fleetwood Mac",
                        SongNode("Lovely Day", "Bill Withers"))))

# print_linked_list(remove_song(playlist, "Dreams"))
# print_linked_list(remove_song(playlist, "sos"))
# print_linked_list(remove_song(playlist, "Lovely day"))


'''    
Problem 4: On Repeat
A variation of the two-pointer technique introduced in previous units is to have a slow and a fast pointer that increment at different rates.

We would like to check whether our playlist loops or not. Given the head of a linked list playlist_head, return True if the playlist has a cycle in it and False otherwise. A linked list has a cycle if at some point in the list, the node’s next pointer points back to a previous node in the list.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    M - Match:
        2 pointers (Floyd's Cycle Detection Algorithm): use 'slow' and 'fast' pointers to traverse the list
    P - Plan
        High-level: 

        Steps: 
            1. init 2 pointers 'slow' and 'fast', pointing to the head
            2. loop thru the entire list:
                1. move 'slow' by 1 step and 'fast' by 2 steps
                2. if 'slow' and 'fast' meet, the playlist has a cycle, 
                thus, return True 
            3. If the fast pointer reaches the end of the list, 
                so that fast != slow, return False (no cycle).
    I - Implement
'''
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist 
        self.next = next

def on_repeat(playlist_head):
    slow, fast = playlist_head, playlist_head # both starts at the head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    
    return False
# Example Usage:
song1 = SongNode("GO!", "Common")
song2 = SongNode("N95", "Kendrick Lamar")
song3 = SongNode("WIN", "Jay Rock")
song4 = SongNode("ATM", "J. Cole")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2
# song1 = None

# print(on_repeat(song1))

''''
Problem 5: Looped
Given the head of a linked list playlist_head that may contain a cycle, use the fast and slow pointer method to return the length of the cycle. If the list does not contain a cycle, return 0.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
U - Understand
        I - Input - head of a linked list 'playlist_head'
        O - Output - the length of the cycle, or return 0 if no cycle
        C - constraints/considerations
        E - example/edge cases
        Clarifying questions to ask yourself:
            What exactly do we mean by “cycle length”?
            What happens if the list has only one node with a cycle to itself?
    M - Match:
        - 2 pointers (Floyd's Cycle Detection Algorithm): use 'slow' and 'fast' pointers to traverse the list
        - measure the length of the cycle
    P - Plan
        High-level: 

        Steps: 
            1. init 2 pointers 'slow' and 'fast', pointing to the head
            2. Cycle detection (Floyd’s Tortoise and Hare) 
            loop thru the entire list:
                - move 'slow' by 1 step and 'fast' by 2 steps
                1. if 'slow' and 'fast' meet, the playlist has a cycle,
                3.Measuring cycle length: 
                    After detecting the cycle:
                        - Keep slow fixed.
                        - Move fast forward by 1 each step.
                        - Count the number of steps until fast meets slow again.
                    That count is the cycle length.
                    return cycle length.
            4. return: If no cycle: return 0.

        Pseudocode (with explanations)
        function loop_length(playlist_head):
            1. Initialize two pointers:
                slow ← playlist_head
                fast ← playlist_head

            2. Traverse the linked list using the fast & slow pointers:
                while fast is not null AND fast.next is not null:
                    slow ← slow.next            // move slow by 1 step
                    fast ← fast.next.next      // move fast by 2 steps

                    if slow == fast:           // cycle detected
                        // Step 3: find the cycle length
                        Initialize counter ← 1
                        fast ← fast.next       // move fast by 1 step

                        while fast != slow:
                            fast ← fast.next
                            counter ← counter + 1

                        return counter         // length of the cycle

            3. If the loop finishes without slow == fast:
                return 0                       // no cycle detected
    I - Implement:
    R - Review your solution
    E - solution's time complexity is O(n) 
            Detect cycle: O(n)
            Count cycle length: O(c) ⟹ O(n)
            So total time complexity: O(n)
        space complexity O(1) 
            - Use a fixed number of pointers: slow, fast, and counter.
            - No additional data structures (no hash sets, no recursion stack, etc).
        think critically about the advantages and disadvantages of chosen approach.
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

def loop_length(playlist_head):
    # 1. Initialize two pointers:
    slow = playlist_head
    fast = playlist_head
    # 2. Traverse the linked list using the fast & slow pointers:
    while fast and fast.next:
        slow = slow.next    # move 'slow' by 1 step
        fast = fast.next.next # move 'fast' by 2 steps
        if slow == fast:
            # Step 3: find the cycle length:
                # Once slow == fast, fix slow in place.
                # init 'counter' with the value of 1
                # use another loop to Move fast (or another pointer) around the cycle until it meets slow again, counting steps.  
            counter = 1
            fast = fast.next
            while fast != slow:
                fast = fast.next
                counter += 1                                
            return counter
    # if we exit the loop without finding a cycle, or other words, 
    # If the loop finishes without slow == fast:
    return 0

# Examples usage
song1 = SongNode("Wein", "AL SHAMI")
song2 = SongNode("Si Ai", "Tayna")
song3 = SongNode("Qalbi", "Yasser Abd Alwahab")
song4 = SongNode("La", "DYSTINCT")
song1.next = song2
song2.next = song3
song3.next = song4
song4.next = song2
# print(loop_length(song1))

# Empty list (playlist_head is null)
empty = None
# print(loop_length(empty))

# Single node pointing to itself (cycle length 1)
s_node = SongNode("Song ", None)
s_node.next = s_node
# print(loop_length(s_node))

'''
## Problem 6: Volume Control
You are working as an engineer normalizing volume levels on songs. Given the head of a singly linked list with integer values song_audio representing volume levels at different points in a song, return the number of critical points. A critical point is a local minima or maxima.

    - The head and tail nodes are not considered critical points.
    - A node is a local minima if both the next and previous elements are greater than the current element
    - A node is a local maxima if both the next and previous elements are less than the current element.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
    U - Understand
        I - Input - the head of a singly linked list with integer values 'song_audio' representing volume levels at different points in a song
        O - Output - the number of critical points. A critical point is a local minima or maxima.
        C - constraints/considerations 
            - The head and tail nodes are not considered critical points.
            - at least 3 nodes: There can't be any critical points if there are less than 3 nodes
        E - example/edge cases
            edge cases: 
            - at least 3 nodes: There can't be any critical points if there are less than 3 nodes
            if less than 3 nodes return 0

    M - Match: 
    Traversal: Traverse the list while comparing the current node’s value with its previous and next nodes to identify critical points.
    P - Plan
        High-level: 
            General Idea: We will traverse the linked list with three pointers (previous, current, and next). For each node, check if it is a local minima or maxima by comparing its value with its neighbors.
        Steps: 
        1. Init 3 pointers: prev, cur and next
            if less than 3 nodes return 0
            init 'counter' with the value 0
        2. use loop to travese the LL 'while next':
        at each iteration check: 
            - if 'cur' is maxima or minima, increase the counter
            - Move all pointers one step forward and continue until next_node becomes None         
        3. return counter

    I - Implement
    R - Review
    E - Evaluate  '''
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

def count_critical_points(song_audio):
    if (not song_audio) or (not song_audio.next) or (not song_audio.next.next):
        return 0  # There can't be any critical points if there are less than 3 nodes
    before = song_audio
    current = song_audio.next
    after = current.next
    count = 0
    while after:         
        if (current.value < before.value and current.value < after.value) or (current.value > before.value and current.value > after.value):
            count += 1
            # print(count)
        # Move all pointers one step forward and continue until next_node becomes None
        before = current
        current = after
        after = after.next
    # return count after while loop is done
    return count	
'''
# Example Usage:
song_audio = Node(5, Node(3, Node(1, Node(2, Node(5, Node(1, Node(2)))))))

print(count_critical_points(song_audio))

# EDGE CASE 
# Expected Output: 0  Explanation: A single node can't be a critical point.
song_audio_single = Node(5)
print(count_critical_points(song_audio_single))

song_audio_two = Node(5, Node(3))
print(count_critical_points(song_audio_two))

# EDGE CASE
# Input: song_audio = Node(5, Node(5, Node(5)))
# Output: 0
# Explanation: All nodes have the same value, so no critical points exist.
song_audio_same = Node(5, Node(5, Node(5)))
print(count_critical_points(song_audio_same))
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