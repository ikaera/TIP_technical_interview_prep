
'''
Problem 1: NFT Name Extractor
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

    U - Understand
        I - Input: list of dictionaries
        O - Output: list of all NFT names 
        C - constraints/considerations rules and limits, or assumptions
            each dict will have a 'name' key with a value
        E - example/edge cases
                # Example usage:
                nft_collection = [
                    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
                    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
                    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
                ]
            Edge cases: 
                empty list, verify that 'name' key exist

    P - Plan
        High-level: 
            Loop thru the input list of dict, 
            pull and take out the value of the key 'name', 
            append it to the result list and return it. 
        Steps: 
            1. init empty list 
            2. iterate thru the list
                1. pull the value of key 'name
                2. append this value to the results list 
            3. return the resuls
    I - Implement
'''

def extract_nft_names(nft_collection):
    result = []  # constant  O(1)
    for item in nft_collection: # O(n)
        name = item.get('name', 'name is missing')  # Uses default if missing
        result.append(name) # constant  O(1)
    return result # constant  O(1)
'''O(n) time and O(n) space
Space Complexity: O(n)
The result list grows linearly with the input size (stores one name per NFT).
If there are n NFTs, you need space for n names.
Analogy: Your notebook needs one page per book title'''
# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

'''
Problem 2: NFT Collection Review
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

Task:

Review the provided code and identify the bug(s).

Explain what the bug is and how it affects the output.

Refactor the code to fix the bug(s) and provide the correct implementation.
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