# Week# Week_5
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# apollo = Villager("Apollo", "Eagle", "pah")
# print(apollo.name)
# print(apollo.species) 
# print(apollo.catchphrase)
# print(apollo.furniture)
    def add_item(self, item_name):
        valid = {"acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"}

        if item_name in valid:
            self.furniture.append(item_name)
        
alice = Villager("Alice", "Koala", "guvnor")
# print(alice.furniture)

alice.add_item("acoustic guitar")
# print(alice.furniture)

alice.add_item("cacao tree")
# print(alice.furniture)

alice.add_item("nintendo switch")
# print(alice.furniture)

# Problem 3: Group by Personality

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    # ... methods from previous problems
	
def of_personality_type(townies, personality_type):
    result = []
    for t in townies:
        if t.personality == personality_type:
            result.append(t.name)
    return result

isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# Problem 4: Telephone
class Villager:
    def __init__(self, name, species, personality, catchphrase, neighbor=None):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
        self.neighbor = neighbor
    # ... methods from previous problems
	
def message_received(start_villager, target_villager):
    neigh = start_villager.neighbor
    while neigh is not None:
        if neigh == target_villager:
            return True
        neigh = neigh.neighbor
    
    return False


isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
tom_nook = Villager("Tom Nook", "Raccoon", "Cranky", "yes, yes")
kk_slider = Villager("K.K. Slider", "Dog", "Lazy", "dig it")
isabelle.neighbor = tom_nook
tom_nook.neighbor = kk_slider
 # isa -> kk
# print(message_received(isabelle, kk_slider))
# print(message_received(kk_slider, isabelle))

# neigh = start.neighbor
# while neigh isnt none
#  if neigh is target: return true
#  neigh = neigh.neighbor
# return false

# Problem 5: Linked Up
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

# Problem 6: Got One!
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head:
        # print("I caught a "+head.fish_name+"!")
        return head.next
    else:
        # print("Aw! Better luck next time!")
        return None

# Example Usage:
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

# Problem 7: Fishing Probability
def fish_chances(head, fish_name):
    if not head:
        return 0
    curr = head
    total = 0
    fish = 0
    while curr is not None:
        if curr.fish_name == fish_name:
            fish += 1
        total += 1
        curr = curr.next
    return round(fish / total, 2)
# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))
fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# print(fish_chances(fish_list, "Dace"))
# print(fish_chances(fish_list, "Rainbow Trout"))





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