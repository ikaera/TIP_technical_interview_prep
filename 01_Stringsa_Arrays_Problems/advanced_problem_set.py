'''
Problem 1: Hunny Hunt
Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.
    U - Understand
        I - Input = list items and a target value as parameters
        O - Output = index of the target item or -1 if target is not found
        C - constraints/considerations = do not use any built-in functions
        E - example/
		
		    edge cases: 
                list is empty, return -1
				
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
def linear_search(lst, target):
	size = len(lst)
	for i in range(size):
		if lst[i] == target:
			return i
	# if target not found return -1 outside of for loop
	return -1
# Example Usage:

items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
target = 'hunny'
# print(linear_search(items, target))

items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
# print(linear_search(items, target))

'''
Example Output:
3
-1
'''

'''
Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
Tiger has developed a new programming language Tiger with only four operations and one variable tigger.
    - bouncy and flouncy both increment the value of the variable tigger by 1.
    - trouncy and pouncy both decrement the value of the variable tigger by 1.
Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.
    
    U - Understand
        I - Input = a list of strings `operations` containing a list of operations, 
        O - Output = return the final value of tiger after performing all the operations.
        C - constraints/considerations
        E - example/
		    HAPPY CASE
            Input: operations = ["trouncy", "flouncy", "flouncy"]
            Expected Output: 2
            Explanation: The operations are performed as follows:
            Initially, tigger = 1.
            trouncy: tigger is decremented by 1, tigger = 0.
            flouncy: tigger is incremented by 1, tigger = 1.
            flouncy: tigger is incremented by 1, tigger = 2.

            Input: operations = ["bouncy", "bouncy", "flouncy"]
            Expected Output: 4
            Explanation: The operations are performed as follows:
            Initially, tagger = 1.
            bouncy: tigger is incremented by 1, tigger = 2.
            bouncy: tigger is incremented by 1, tigger = 3.
            flouncy: tigger is incremented by 1, tigger = 4.

            EDGE CASE
            Input: operations = ["trouncy"]
            Expected Output: 0
            Explanation: The only operation decrements tigger to 0.
		
        edge cases: If the list is empty, the value of tigger remains 1.
    P - Plan
        High-level: 

        Steps: 
		1. init var tiger with 1
		2. Iterate thru the list 
		3. for each iter:
            if item of the list is "bouncy or flouncy" increment tiger value
			if ite is 'trouncy and pouncy'  decrement the value
		4. return tiger
    I - Implement
'''
def final_value_after_operations(operations):
	tiger = 1
	for operation in operations:
		if operation == 'bouncy' or operation == 'flouncy':
			tiger +=1 
		if operation == 'trouncy' or operation == 'pouncy':
			tiger -=1
	return tiger
# Example Usage:

operations = ["trouncy", "flouncy", "flouncy"]
# print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
# print(final_value_after_operations(operations))

r'''Example Output:
2
4
'''

'''
Problem 6: Vegetable Harvest
Rabbit is collecting carrots from his garden to make a feast for Pooh and friends. Write a function harvest() that accepts a 2D n x m matrix vegetable_patch and returns the number of of carrots that are ready to harvest in the vegetable patch. A carrot is ready to harvest if vegetable_patch[i][j] has value 'c'.

Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.
   
    U - Understand
        I - Input = 2D nxn matrix
        O - Output = number of carrots that are ready to harvest
        C - constraints/considerations - Assume n = len(vegetable_patch) and m = len(vegetable_patch[0]). 0 <= i < n and 0 <= j < m.
        E - example/edge cases
            EDGE CASE
            If the matrix is empty, the function should return 0.
            Example: []
    P - Plan
        High-level: 
           
        Steps: 

    I - Implement
'''
def harvest(vegetable_patch):
	'''Steps: 
        1. Init a counter to keep track of the num of carrots
		2. get n = len(vegetable_patch) and m = len(vegetable_patch[0]) 
		3. Iterate over 2D array
		4. check if element is `c`
            if it is increment the counter
		5. return counter 
	'''
	if not vegetable_patch:
		return []
	counter = 0
	n = len(vegetable_patch)
	m = len(vegetable_patch[0])
	for i in range(n):
		for j in range(m):
			if vegetable_patch[i][j] == 'c':
				counter += 1
	return counter
	# outside of the loops return counter 
# Example Usage:
vegetable_patch = [
	['x', 'c', 'x'],
	['x', 'x', 'x'],
	['x', 'c', 'c'],
	['c', 'c', 'c']
]
# print(harvest(vegetable_patch))
# print(harvest([]))

# Example Output: 6

####################################
''' Problem 7: Eeyore's House
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1.   

    U - Understand
        I - Input: consists of 2 int lists(arrays) `pile1` and `pile2` and positive int k
        O - Output:  return the number of good pairs. 
        C - constraints/considerations
            A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. 
			Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1 (The problem assumes the arrays are non-empty and contain positive integers, as stick lengths cannot be zero.).
        E - example/edge cases
            HAPPY CASE
            Input: pile1 = [1, 3, 4], pile2 = [1, 3, 4], k = 1
            Expected Output: 5

            Input: pile1 = [1, 2, 4, 12], pile2 = [2, 4], k = 3
            Expected Output: 2

            EDGE CASE
            Input: pile1 = [2, 4, 6], pile2 = [1, 1, 1], k = 2
            Expected Output: 9

            Input: pile1 = [], pile2 = [1, 2, 3], k = 1
            Expected Output: 0
    P - Plan
        High-level: Use for loop to iterate through pile1; for each item iterate through each item in pile2. each time check if pile1[i] is devisable by pile2[j] *k. Along the way count the number of good pairs.
        Steps: 

    I - Implement
'''
def good_pairs(pile1, pile2, k):
	num_good_pairs = 0
	for i in range (len(pile1)):
		for j in range(len(pile2)):
			if pile1[i] % (pile2[j] * k) == 0:
				num_good_pairs += 1
	return num_good_pairs


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
# print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
# print(good_pairs(pile1, pile2, k))
# print(good_pairs([], [1,2], 1))

'''Example Output:
5
2'''

##############################
'''Problem 8: Local Maximums
Write a function local_maximums() that accepts an n x n integer matrix grid and returns an integer matrix local_maxes of size (n - 2) x (n - 2) such that:

local_maxes[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
    
    U - Understand
        I - Input: 'n x n' int matrix `grid`
        O - Output: (n-2) x (n-2) matrix `local_max`, where each element represents the maximum value found in the 3 x 3 sub-matrix centered around each element (i+1, j+1) in grid.
            {Namely, we want to find the largest value in every contiguous (or adjacent or Neighboring) 3 x 3 matrix in a given grid.}  
        C - constraints/considerations
            Q: How do we determine the size of the output matrix?
                A: The output matrix local_maxes will be of size (n - 2) x (n - 2) because the 3 x 3 submatrix cannot be centered around the outermost rows and columns.
            Q: What if the input matrix is smaller than 3 x 3?
                A: The function assumes that n >= 3, so it does not handle cases where the grid is smaller than 3 x 3.
            Q: What should the function return if the input grid has the minimum size of 3 x 3?
                A: For a 3 x 3 grid, the output will be a 1 x 1 matrix containing the maximum value of the entire grid.
            The function local_maximums() should take an n x n integer matrix grid and return an (n-2) x (n-2) integer matrix local_maxes where each element is the largest value in every contiguous 3 x 3 sub-matrix of grid.
        E - example/edge cases
            HAPPY CASE
            Input: 
            [   
                [9,9,8,1],
                [5,6,2,6],
                [8,2,6,4],
                [6,2,2,2]
            ]
                Expected Output: 
                [   
                    [9,9],
                    [8,6]
                ]

            Input: 
            [   
                [1,1,1,1,1],
                [1,1,1,1,1],
                [1,1,2,1,1],
                [1,1,1,1,1],
                [1,1,1,1,1]
            ]
                Expected Output: 
                [   
                    [2,2,2],
                    [2,2,2],
                    [2,2,2]
                ]

            EDGE CASE
            Input: 
            [    
                [0,0,0],
                [0,0,0],
                [0,0,0]
            ]
                Expected Output: 
                [    
                    [0]
                ]

            Input: 
            [    
                [1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]
            ]
                    Expected Output: 
                    [    
                        [11,12],
                        [15,16]
                    ]
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
def local_maximums(grid):
	local_maxes = []
	size = len(grid)
	for i in range(size - 2):
		row_maxes = []
		for j in range(size - 2):
			max_value = max(grid[x][y] for x in range(i, i + 3)  for y in range(j, j +3))
			'''
			# Extract the 3x3 sub-matrix starting at (i, j)
            max_val = -float('inf')  # Start with a very small number
            for x in range(i, i + 3):  # Rows: i, i+1, i+2
                for y in range(j, j + 3):  # Cols: j, j+1, j+2
                    max_val = max(max_val, grid[x][y])  # Update max if needed'''
			row_maxes.append(max_value)
		local_maxes.append(row_maxes)
	return local_maxes		

# Example Usage:
grid = [
	[9, 9, 8, 1],
	[5, 6, 2, 6],
	[8, 2, 6, 4],
	[6, 2, 2, 2]
]
# print(local_maximums(grid))

grid = [
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 2, 1, 1],
	[1, 1, 1, 1, 1],
	[1, 1, 1, 1, 1]
]
# print(local_maximums(grid))

# print(local_maximums([]))

grid0 = [
	[0,0, 0],
	[0,0, 0],
	[0,0, 0]
]
# print("Grid containing only 0s:", local_maximums(grid0))
'''Example Output:

[[9, 9], [8, 6]]
[[2, 2, 2], [2, 2, 2], [2, 2, 2]]'''