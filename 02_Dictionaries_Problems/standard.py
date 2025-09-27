"""
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

Example Usage:

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  
Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}
"""
def get_artist_info(artist, festival_schedule):
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return {"message": "Artist not found"}

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}
    
# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))

"""
Problem 4: Scheduling Conflict
Demand for your festival has exceeded expectations, so you're expanding the festival to span two different venues. Some artists will perform both venues, while others will perform at just one. To ensure that there are no scheduling conflicts, implement a function identify_conflicts() that accepts two dictionaries venue1_schedule and venue2_schedule each mapping the artists playing at the venue to their set times. Return a dictionary containing the key-value pairs that are the same in each schedule.

"""
def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}
    for artist, time in venue1_schedule.items():
        if artist in venue2_schedule and time == venue2_schedule[artist]:
            result[artist] = time
    return result
# test: 
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

# print(identify_conflicts(venue1_schedule, venue2_schedule))

# ------------------------------------------------
# TIP102 Unit 2 Session 2 Standard
"""
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

"""


def most_endangered(species_list):
    # Initialize two variables:
    min_population = float('inf')
    most_endangered_name = ''
    # 2. Loop through each species in species_list:
    for specie in species_list: 
        if specie['population'] < min_population:
            min_population = specie['population']
            most_endangered_name = specie['name']
            
    # 3. After the loop, return most_endangered_name
    
    return most_endangered_name


# Example Usage:

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 72
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10 
#     }
# ]
species_list = [
    {"name": "SpeciesA", "habitat": "Desert", "population": 100},
    {"name": "SpeciesB", "habitat": "Jungle", "population": 100},
    {"name": "SpeciesC", "habitat": "Ocean", "population": 500}
]
# print(most_endangered(species_list))
'''
Problem 3: Navigating the Research Station
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.
U - Understand
I - Inputs
        I -Inputs
            -string 'station_layout' of length 26 indicating the layout of these observation points 
            (indexed from 0 to 25), you start your journey at the first observation point (index 0)
            -string 'observations' representing the order of required observations
        O - Outputs
            - returns the total time it takes to visit all the required observation points in the given order with one movement.
        C - Constains/consideration
            - 
        E - Examples/edge cases
            Examples: 
                -  
            Edge case: 
            🔠 Inputs:
                station_layout: "abcdefghijklmnopqrstuvwxyz"
                Each character is a station in a row, like this:                
                Index:   0  1  2  3  4  5  6  7  8  ... 25
                Layout:  a  b  c  d  e  f  g  h  i  ... z
                
                observations: "cba"  
                Start → 'c' → 'b' → 'a'
                  0      2     1     0
                  |------|-----|-----|
                  2     +1    +1  =  4 units of time   
    P - Plan
        
'''
def navigate_research_station(station_layout, observations):
    #1. Create a mapping of each character in station_layout to its index, 
    # other words, create dictionary 'layout_dict' to map each letter in 'station_layout' to its index
        # This allows quick lookup of where each observation point is.
    layout_dict = {}
    for index, char in enumerate(station_layout):
        layout_dict[char] = index
    # 2. Initialize current_index to 0 and total_time to 0
    current_index = 0
    total_time = 0
    # 3. Iterate though 'observatinos', For each character c in observations:
    for c in observations:
        # - Use the mapping to find the target index of character c.
        target_index =  layout_dict[c]
        # - Compute the distance = abs(current_index - target_index)
        distance = abs(current_index - target_index) 
        # - Add the distance to total_time
        total_time += distance
        # - Update current_index = target_index
        current_index = target_index
    # 4. Return 'total_time'  as a result
    return total_time

# Test Example Usage:

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

# print(navigate_research_station(station_layout1, observations1))  
# print(navigate_research_station(station_layout2, observations2))

'''
Problem 4: Prioritizing Endangered Species Observations
In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.

Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.
'''
def prioritize_observations(observed_species, priority_species):
    # 1. Create an empty dictionary called count_map.
    count_map = {}
    '''{
            "bluejay": 1,
            "sparrow": 1,
            "cardinal": 1,
            "robin": 1,
            "crow": 1
            }'''
    # 2. Count the occurrences of each element in observed_species
    # For each species in observed_species:
    for species in observed_species: 
        # - If species is in count_map, increment its count.
        if species in count_map:
            count_map[species] +=1    
        # - Otherwise, set count_map[species] = 1
        else: 
            count_map[species] = 1

    # 3. Create an empty list called result.
    result_list = []
    # 4. For each species in priority_species:
    for species in priority_species:
    #   - If species exists in count_map:
        if species in count_map:
    #         - Append that species count_map[species] times to result
                # use The extend() method that adds the specified list elements (or any iterable) to the end of the current list.
        # ?result_list.append(species)
            result_list.extend([species] * count_map[species])
    #         - Remove it from count_map - use 'del'
            del count_map[species] # Remove the element from count after processing
    # Remaining elements in observed_species that are not in priority_species
    remaining_list = []
    for species in observed_species:
        if species in count_map:
            remaining_list.append(species)
    # 5. Sort 'remaining_list' alphabetically.
    remaining_list.sort()
    # 6. For each species in sorted remaining keys:
    #     - Append that species count_map[species] times to result
    result_list.extend(remaining_list)
    # 7. Return result.
    return result_list

# Example usage
observed_species2 = [ "zzz", "bluejay", "sparrow", "cardinal", "robin", "crow", "zebra", "aaa"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

# print(prioritize_observations(observed_species2, priority_species2)) 

'''
Problem 5: Calculating Conservation Statistics
You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.
'''

def distinct_averages(species_populations):
    # Initialize an empty set called averages
    averages_set = set()
    # Sort species_populations into sorted_pops
    sorted_populations = sorted(species_populations)
    # While sorted_pops is not empty:
    while sorted_populations:
    #   remove  min_val = first element of sorted_pops
        # min_val = sorted_populations[0]
        min_val = sorted_populations.pop(0)
    #   remove  max_val = last element of sorted_pops
        # max_val = sorted_populations[-1]
        max_val = sorted_populations.pop(-1)
    #     avg = (min_val + max_val) / 2
        average = (min_val + max_val) / 2
    #     Add avg to averages set
        averages_set.add(average)
    #   Remove first and last elements from sorted_pops
        # sorted_populations.pop(0)
        # sorted_populations.pop(-1)
    # Return size of averages set
    return len(averages_set)

# Example Usage:
species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

# print(distinct_averages(species_populations1))
# print(distinct_averages(species_populations2)) 

'''
Example Output:

2
Example 1 Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

1
Example 2 Explanation:
There is only one average to be calculated after removing 1 and 100, 
so we return 1.
'''

'''Standard Problem Set Version 2
Problem 1: Space Crew
Given two lists of length n, crew and position, map the space station crew to their position on board the international space station.

Each crew member crew[i] has job position[i] on board, where 0 <= i < n and len(crew) == len(position).

Hint: Introduction to dictionaries
    
    U - Understand
        I - Input
        O - Output 
        C - constraints/considerations
        E - example/edge cases (see bellow)
    P - Plan
        High-level: 

        Steps: 

    I - Implement
'''
def space_crew(crew, position):
    # step 1
    crew_position_dict = {}
    # step 2: Iterate thru the lists 
    n = len(crew)
    for i in range(n):
        key = crew[i]
        value = position [i]
        crew_position_dict[key] = value
    # outside of for loop return
    return crew_position_dict

# Example Usage:

exp70_crew = ["Andreas Mogensen", "Jasmin Moghbeli", "Satoshi Furukawa", "Loral O'Hara", "Konstantin Borisov"]
exp70_positions = ["Commander", "Flight Engineer", "Flight Engineer", " Flight Engineer", "Flight Engineer"] 

ax3_crew = ["Michael Lopez-Alegria", "Walter Villadei", "Alper Gezeravci", "Marcus Wandt"]
ax3_positions = ["Commander", "Mission Pilot", "Mission Specialist", "Mission Specialist"]

# print(space_crew(exp70_crew, exp70_positions))
# print(space_crew(ax3_crew, ax3_positions))
r'''Example Output:

{
    "Andreas Mogensen": "Commander",
    "Jasmin Moghbeli": "Flight Engineer",
    "Satoshi Furukawa": "Flight Engineer",
    "Loral O'Hara": "Flight Engineer",
    "Konstantin Borisov": "Flight Engineer",
}

{
    "Michael López-Alegría": "Commander",
    "Walter Villadei": "Mission Pilot",
    "Alper Gezeravcı": "Mission Specialist",
    "Marcus Wandt": "Mission Specialist"
}'''
####################################

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


###########################
