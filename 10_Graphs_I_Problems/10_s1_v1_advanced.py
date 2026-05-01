# week_10
# Problem 1: There and Back
def bidirectional_flights(flights):
    
    for row in range(len(flights)):
        # print("row: ", row)
        for col in flights[row]:
            # print("col: ", col)
            if row not in flights[col]:                
                return False
        # print("#####")
    
    return True
#testcases
flights1 = [[1, 2], #0
            [0],    #1
            [0, 3], #2
            [2]]    #3
flights2 = [[1, 2], #0
            [],     #1 
            [0],    #2
            [2]]    #3 

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))
# Example Output: True False   
'''
Problem 2: Find Center of Airport

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
Problem Set Version 2
Problem 1: The Feeling is Mutual
'''
def is_mutual(celebrities):
    n = len(celebrities)
    for row in range(n):
        for col in range(n):
            # check condition
            if celebrities[row][col] != celebrities[col][row]:
                return False
    
    return True

celebrities1 = [
                [0, 1, 1, 0],
                [1, 0, 1, 0],
                [1, 1, 0, 1],
                [0, 0, 1, 0]]

celebrities2 = [
                [0, 1, 1, 0],
                [1, 0, 0, 0],
                [1, 1, 0, 1],
                [0, 0, 0, 0]]

# print(is_mutual(celebrities1))
# print(is_mutual(celebrities2))
# Example Output:
# True
# False
# complexity time O(n^2) and space O(1)
"""
clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]
"""

# iterating through clients
# Y = 0
# J = 1
# F = 2
# B = 3
# M = 4
# A = 5

#     F  Y  M  B  A  J
#  F [0, 0, 0, 0, 1, 1],  # Fred Armisen
#  Y [0, 0, 0, 0, 0, 1],  # Yalitza Aparicio
#  M [0, 0, 0, 1, 1, 0],  # Margaret Cho
#  B [0, 0, 1, 0, 1, 1],  # Bowen Yang
#  A [1, 0, 1, 1, 0, 0],  # Ali Wong
#  J [1, 1, 0, 1, 0, 0]   # Julio Torres
#

# Problem 2: Network Lookup
def get_adj_matrix(clients):
    # iterate through clients, making id map
    client_id = {}
    id = 0
    for a, b in clients:
        if a not in client_id:
            client_id[a] = id
            id += 1
        
        if b not in client_id:
            client_id[b] = id
            id += 1

    #create matrix
    n = id
    client_matrix = [[0 for _ in range(n)] for _ in range(n)]
    # [0,0,0,..., n]
    # second for copies it n times
    matrix = [[0] * n] * n
    # print("M1")
    # for row in matrix:
    #     print(row)

    # # print("\nM2")
    # matrix = []
    # for _ in range(n):
    #     row = []
    #     for _ in range(n):
    #         row.append(0)
    #     matrix.append(row)

    # for row in matrix:
    #     pass
    #     # print(row)
    
    # # return 0,0
clients = [
            ["Yalitza Aparicio", "Julio Torres"], 
            ["Julio Torres", "Fred Armisen"], 
            ["Bowen Yang", "Julio Torres"],
            ["Bowen Yang", "Margaret Cho"],
            ["Margaret Cho", "Ali Wong"],
            ["Ali Wong", "Fred Armisen"], 
            ["Ali Wong", "Bowen Yang"]]

# id_map, adj_matrix = get_adj_matrix(clients)
# print(id_map)
# print(adj_matrix)