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
def transpose(matrix):
    cols = len(matrix[0])
    rows = len(matrix)
    ans = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for row in range(rows):
        for col in range(cols):
            ans[col][row] = matrix[row][col]
    return ans

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
# print( transpose(matrix))


# Problem 2: Two-Pointer Reverse List


def reverse_list(lst):
        # init 2 pointers
        start = 0
        end = len(lst) - 1
        # while loop until end > start
        while end > start:
            #swap
            lst[start], lst[end] = lst[end], lst[start]

            # move pointers     
            start += 1
            end -= 1
        return lst

    
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
# print(reverse_list(lst))

def remove_dupes(items):
    if not items:
        return 0
    
    slow = 0
    for fast in range(1, len(items)):
        if items[fast] != items[slow]
            slow += 1
            items[slow] = items[fast]
    return slow + 1 