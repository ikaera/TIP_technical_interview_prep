
'''Standard Problem Set Version 1
Problem 1: Graphing Flights    
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
flights = {
    'JFK': ['LAX', 'DFW'] ,
    'LAX': ['JFK'],
    'DFW': ['ATL', 'JFK'],
    'ATL': ['DFW']
}
# Example Usage:

# print(list(flights.keys()))
# print(list(flights.values()))
# print(flights["JFK"])
''' Problem 2: There and Back   
U - Understand
    I - Input - flights list
    O - Output - Bol: T or F
    C - constraints/considerations
    E - example/edge cases: no or only 1 flight => F
P - Plan
    High-level: 

    Steps: 

I - Implement
'''
def bidirectional_flights(flights):
    n = len (flights)
    for row in range (n):
        for col  in flights[row]:
            if row not in flights[col]:
                return False
    return True

# flights1 = [[1, 2], 
#             [0], 
#             [0, 3], 
#             [2]]
# flights2 = [[1, 2], 
#             [], 
#             [0], 
#             [2]]

# print(bidirectional_flights(flights1))
# print(bidirectional_flights(flights2))

''' Problem 3: Finding Direct Flights    
U - Understand
    I - Input - an adjacency matrix flights and an integer source representing the destination a customer is flying out of
    O - Output - a list of all destinations the customer can reach from source on a direct flight.
    C - constraints/considerations: 
    E - example/edge cases: 
        an empty matrix 'flights' => []
P - Plan
    High-level: loop through the row of flights
    Steps: 
        - init results_list
        - for destination in flights[source]: 
            - if flight[source][destination] == 1
                results_list.append(destination)
        - return results_list

I - Implement
'''
def get_direct_flights(flights, source):
    results_list = []
    n = len(flights[source])
    for dest in range(n):
        if flights[source][dest] == 1:
            results_list.append(dest)
    return results_list

# flights = [
#             [0, 1, 1, 0],
#             [1, 0, 0, 0],
#             [1, 1, 0, 1],
#             [0, 0, 0, 0]]

# print(get_direct_flights(flights, 2))
# print(get_direct_flights(flights, 3))

'''    
Problem 4: Converting Flight Representations
Given a list of edges flights where flights[i] = [a, b] denotes that there exists a bidirectional flight (incoming and outgoing flight) from city a to city b, return an adjacency dictionary adj_dict representing the same flights graph where adj_dict[a] is an array denoting there is a flight from city a to each city in adj_dict[a].

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
def get_adj_dict(flights):
    pass

flights = [['Cape Town', 'Addis Ababa'], ['Cairo', 'Lagos'], ['Lagos', 'Addis Ababa'], 
            ['Nairobi', 'Cairo'], ['Cairo', 'Cape Town']]
print(get_adj_dict(flights))

'''
Example Output:
{
    'Cape Town': ['Addis Ababa', 'Cairo'],
    'Addis Ababa': ['Cape Town', 'Lagos'],
    'Lagos': ['Cairo', 'Addis Ababa'],
    'Cairo': ['Lagos', 'Nairobi', 'Cape Town'],
    'Nairobi': ['Cairo']
}
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