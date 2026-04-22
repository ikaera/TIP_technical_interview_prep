# Week
'''
U - Understand
    I - Input - a list of lists sandwich
    O - Output - int total number of sandwich layers.
    C - constraints/considerations
    E - example/edge cases - an empty list => 0
P - Plan
    High-level: 

    Steps: 

I - Implement
'''
def count_layers(sandwich):
    # base case: if list is empty => 0
    if not sandwich:
        return 0
    # base case: Only one layer exists, no nested list => 1
    if len(sandwich) == 1:
        return 1
    # recursive case:     
    return 1 + count_layers(sandwich[1])

# Example Usage:

sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))

# complexity: time O(n) and space O(n) n si layers

'''    
U - Understand
    I - Input - string of orders
    O - Output -> str
    C - constraints/considerations
    E - example/edge cases -> ""
P - Plan
    High-level: 

    Steps: 

I - Implement
'''

'''
'''

def reverse_orders(orders):
    # Base Case: if string is empty, return empty string
    if not orders:
        return ""
    
    words = orders.split() # eg. "Bagel Sandwich Coffee" => ["Bagel", "Sandwich", "Coffee"]
    
    def helper_function(l, r):
        if l >= r:      # Base case: if l and r are the same or have crossed, we are done
            return
        
        # swap words at l and r (inwards e.g l = 0, r = 2 => swap "Bagel" and "Coffee")
        words[l], words[r] = words[r], words[l]
        
        helper_function(l + 1, r - 1)
        
    helper_function(0, len(words) - 1)
    return " ".join(words)
        
        
        
# print(reverse_orders("Bagel Sandwich Coffee"))

# Time complexity: O(n) where n -> no. of words
# Space complexity: O(n)

def can_split_coffee(coffee, n):
    total_sum = sum(coffee)    
    return total_sum % n == 0
       
# Example Usage:

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))
# Example Output: 
# True
# False