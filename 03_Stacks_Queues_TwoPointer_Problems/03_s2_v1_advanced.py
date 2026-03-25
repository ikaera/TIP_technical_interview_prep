# Week 3: Stacks, Queues, Two Pointer
'''
Problem 1: Blueprint Approval Process
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

'''
'''
from collections import deque

def blueprint_approval(blueprints):
    queue = deque(blueprints)
    result=[]
    # blueprints.sort()
    # for b in blueprints:
    #     queue.append(b)
    #     add_el = queue.popleft()
    #     result.append(add_el)
    
    while queue:
        current = queue.popleft()

        # if queue is empty, append it or if not empty then do conditional
        if not queue or current <= min(queue):
            result.append(current)
        else:
            queue.append(current)

    return result

# print(blueprint_approval([3, 5, 2, 1, 4])) 
# print(blueprint_approval([7, 4, 6, 2, 5]))    


def build_skyscrapers(floors):
    counter = 1
    for i in range(1, len(floors)):
        if floors[i-1] < floors[i]:
            counter+=1
    return counter
        
# print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
# print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
# print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 

#u- 
 
def filter_sustainable_brands(brands, criterion):
    result = []
    for brand in brands: 
        if criterion in brand["criteria"]:
            result.append(brand["name"])

    return result

# complexity  time 0(n) and space 0(n)



brands = [
    {"name": "EcoWear", "criteria": ["eco-friendly", "ethical labor"]},
    {"name": "FastFashion", "criteria": ["cheap materials", "fast production"]},
    {"name": "GreenThreads", "criteria": ["eco-friendly", "carbon-neutral"]},
    {"name": "TrendyStyle", "criteria": ["trendy designs"]}
]

brands_2 = [
    {"name": "Earthly", "criteria": ["ethical labor", "fair wages"]},
    {"name": "FastStyle", "criteria": ["mass production"]},
    {"name": "NatureWear", "criteria": ["eco-friendly"]},
    {"name": "GreenFit", "criteria": ["recycled materials", "eco-friendly"]}
]

brands_3 = [
    {"name": "OrganicThreads", "criteria": ["organic cotton", "fair trade"]},
    {"name": "GreenLife", "criteria": ["recycled materials", "carbon-neutral"]},
    {"name": "FastCloth", "criteria": ["cheap production"]}
]

# print(filter_sustainable_brands(brands, "eco-friendly"))
# print(filter_sustainable_brands(brands_2, "ethical labor"))
# print(filter_sustainable_brands(brands_3, "carbon-neutral"))


def count_material_usage(brands):
    result = {}

    for brand in  brands:
        for material in brand["materials"]:
            if material in result:
                result[material] += 1
            else:
                result[material] = 1

    return result
# complexity: time O(n^2) and space O(n)

brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

# print(count_material_usage(brands))
# print(count_material_usage(brands_2))
# print(count_material_usage(brands_3))

def find_trending_materials(brands):
    result = []
    frequency = {}

    for brand in brands:
        for material in brand["materials"]:
            if material in frequency:
                frequency[material] += 1
            else:
                frequency[material] = 1
    
    for key, value in frequency.items():
        if value >= 2:
            result.append(key)

    return result
# complexity time O(n^) and space O(n)
brands = [
    {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
    {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
    {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]}
]

brands_2 = [
    {"name": "NatureWear", "materials": ["hemp", "linen"]},
    {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
    {"name": "GreenFit", "materials": ["linen", "recycled wool"]}
]

brands_3 = [
    {"name": "OrganicThreads", "materials": ["organic cotton"]},
    {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
    {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]}
]

print(find_trending_materials(brands))
print(find_trending_materials(brands_2))
print(find_trending_materials(brands_3))