
'''Problem 1: Counting Treasure
Captain Blackbeard has a treasure map with several clues that point to different locations on an island. Each clue is associated with a specific location and the number of treasures buried there. Given a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations, write a function total_treasures() that returns the total number of treasures buried on the island.    
    U - Understand 
        I - Input = a dictionary treasure_map where keys are location names and values are integers representing the number of treasures buried at those locations,
        O - Output = the total number of treasures
        C - constraints/considerations
        E - example/edge cases 
    P - Plan
        High-level: 
            Iterate thru the keys and at each iteration add each value to get the total num of treasures
        Steps: 

    I - Implement
'''
def total_treasures (treasure_map):
    total = 0
    for location in treasure_map:
        total += treasure_map[location]
    return total    

# Example Usage:
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}

treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}

# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 

r'''Example Output:
15
50
✨ AI Hint: Dictionaries
Key Skill: Use AI to explain code concepts

This question requires you to create a dictionary.

If you are unfamiliar with what a dictionary is, or how to create a dictionary, you can learn about Python dictionaries using a generative AI tool, like this:

"You're an expert computer science tutor. Please explain what a dictionary is in Python, and provide a simple code example of how to create one."

After you get your answer, you can also ask follow up questions:

"How is a dictionary different from a list? Can you show me examples of both?"

✨ AI Hint: Accessing Values in a Dictionary
Key Skill: Use AI to explain code concepts

This question will require you to use keys to access their corresponding values in a dictionary. There are two common ways to access values in a dictionary. Try asking ChatGPT or GitHub copilot:

"You're an expert computer science tutor. Please show me the two most common ways to access values in a dictionary in Python, and explain how each one works."

Then open the next hint to see the answer!

💡 Hint: Dictionary Access options
The two common ways to access values in a dictionary are square bracket notation d[key] and the get() method.

The Unit 2 cheatsheet includes a more thorough breakdown of these two options. If you still feel confused after reviewing the cheatsheet, try asking generative AI to help you understand!

💡 Hint: Accessing Keys, Values, and Key-Value Pairs
This question will require you to loop over a dictionary. We have three options for looping over a dictionary: looping over the keys, values, or key-value pairs. To explore how to access the keys, values, and key-value pairs reference the unit cheatsheet. For specific examples of looping over a dictionary, ask a generative AI tool to provide an example or search for existing examples using a search engine.
'''
############################

'''Problem 2: Pirate Message Check
Taken captive, Captain Anne Bonny has been smuggled a secret message from her crew. She will know she can trust the message if it contains all of the letters in the alphabet. Given a string message containing only lowercase English letters and whitespace, write a function can_trust_message() that returns True if the message contains every letter of the English alphabet at least once, and False otherwise.
    
    U - Understand
        I - Input: a string 'message'
        O - Output: True or False
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 
            Use a set DS to track the unique letters in the message (replace(' ', '')), compare it with a set of all letters in the alphabet. (issubset())  
        Steps: 
            1. Init set of all lowercase letters in English abc
            2. init set from the input string 'message', remove any whitespace 
            3. check if abs set is the subset of the 'message_set' or if message_set is the superset of the 'abc_set'
    I - Implement
'''
def can_trust_message(message):
    abc_set = set('abcdefghijklmnopqrstuvwxyz')
    message.replace(" ", "")
    message_set = set(message.lower())
    return message_set.issuperset(abc_set)
# Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))
# print(can_trust_message("Sphinx of black quartz judge my Vow"))
'''
Example Output:
True
False'''

'''    
    U - Understand
        I - Input: dictionary treasure_map
        O - Output: int total
        C - constraints/considerations:
        E - example/edge cases:
            empty dictionary

    P - Plan
        High-level: 
            iterate thu dictionary and add values
        Steps: 
         - Init total
         - Iterate thru dictionary
            - add up treasure_map[key] 
         - return total   
    I - Implement
'''
def total_treasure(treasure_map):
    total = 0
    for value in treasure_map.values():
        total += value
    return total

# Example Usage:
treasure_map1 = {
    "Cove": 3,
    "Beach": 7,
    "Forest": 5
}
treasure_map2 = {
    "Shipwreck": 10,
    "Cave": 20,
    "Lagoon": 15,
    "Island Peak": 5
}
# print(total_treasures(treasure_map1)) 
# print(total_treasures(treasure_map2)) 

# Example Output: 15  50

'''    
    U - Understand
        I - Input: string message
        O - Output: Boolean
        C - constraints/considerations: 
        E - example/edge cases:
            empty string, 
    P - Plan
        High-level: 
        import string
            print(string.ascii_lowercase)

        Steps: 
         - remove white space use strip()
         - change message to set
         - return size of set == 26
    I - Implement
'''
# def can_trust_message(message):
#     set_msg = set(message)
#     set_msg.remove(' ')
#     return len(set_msg) == 26
def can_trust_message(message):
    for i in range(ord('a'),ord('z')):
        if not (chr(i) in message):
            return False
    return True
# Example Usage:

message1 = "sphinx of black quartz judge my vow"
message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))
# Example Output:
# True False

'''    
    U - Understand
        I - Input: in array  in the range of 1 - n
        O - Output: an array of all the integers that appear twice 
        C - constraints/considerations
        E - example/edge cases:
         an empty array
         no repetition return []
    P - Plan
        High-level: 

        Steps: 
         - init an empty set  
         - array result
         - Loop thu array 
            check if value is in the set
                if yes: result.append(value)
                no: add to the set
         - return result
    I - Implement
'''
def find_duplicate_chests(chests):
    chests_set = set()
    result = []
    for chest in chests:
        if chest in chests_set:
            result.append(chest)
        else:
            chests_set.add(chest)
    return result
# Example Usage:
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))
# Example Output:
# [2, 3]
# [1]
# []
''' 
Problem 4: Booby Trap   
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases
    P - Plan
        High-level: 

        Steps: 
         - 
         - 
         - 
    I - Implement
'''
def can_make_balanced(code):
    pass
# Example Usage:

code1 = "arghh"
code2 = "haha"

# print(can_make_balanced(code1)) 
# print(can_make_balanced(code2)) 
# Example Output:

# True
# Explanation: Select index 4 and delete it: word becomes "argh" and each character has a frequency of 1.

# False