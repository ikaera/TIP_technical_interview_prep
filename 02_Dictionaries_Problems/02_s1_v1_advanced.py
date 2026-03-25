# Week 2: Session 1: Dictionaries

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
def total_treasures(treasure_map):
    return sum(treasure_map.values())

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

# Problem 2: Pirate Message Check

def can_trust_message(message):
    # declare an empty set
    result = set()
    for letter in message:
        if letter.isalpha():
            result.add(letter)
    # len()
    return len(result) == 26

message1 = "sphinx of black quartz judge my vow!!!"
message2 = "trust me"

# print(can_trust_message(message1))
# print(can_trust_message(message2))

# Problem 3: Find All Duplicate Treasure Chests in an Array

def find_duplicate_chests(chests):
    result_dict = {}    
    for chest in chests: 
        if chest not in result_dict: 
            result_dict[chest] = 1
        else: 
            result_dict[chest] += 1
    # Return an array of all the integers that appear twice
    result = []
    for chest, count in result_dict.items():
        if count == 2:
            result.append(chest)
    # result.sort()
    return sorted(result)

# example: 
chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
chests2 = [1, 1, 2]
chests3 = [1]

print(find_duplicate_chests(chests1))
print(find_duplicate_chests(chests2))
print(find_duplicate_chests(chests3))
            
        


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
