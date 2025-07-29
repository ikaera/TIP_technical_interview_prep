'''
P - Plan:
    Detailed steps: 
        ### **Step 1: Main Function Setup**
        1. **Define `search_range` function**  
        - Takes two parameters: `nums` (sorted array) and `target` (value to find).
        - Returns a list `[first_index, last_index]` of the target's positions.

        2. **Edge Case Handling**  
        - Immediately checks if `nums` is empty.  
        - If empty, returns `[-1, -1]` because no elements exist to search.

        ### **Step 2: Helper Function `find_position`**
        1. **Purpose**  
        - A nested helper function to perform binary search for either the **first** or **last** occurrence of `target`.  
        - Takes three arguments:  
            - `nums`: The sorted array.  
            - `target`: The value to search for.  
            - `find_first`: Boolean flag (`True` for first occurrence, `False` for last).  

        2. **Initialize Variables**  
        - `left = 0`, `right = len(nums) - 1`: Sets search boundaries.  
        - `position = -1`: Default return value if `target` is not found.  

        ### **Step 3: Binary Search Execution**
        1. **Loop Until Search Space Exhausted**  
        - While `left <= right`:  
            - **Calculate Midpoint**:  
            ```python
            mid = left + (right - left) // 2  # Prevents integer overflow
            ```
            - **Check Midpoint Value**:
            - If `nums[mid] == target`:  
                - **Store Position**: `position = mid` (records where `target` was found).  
                - **Adjust Search Boundaries**:
                - If `find_first=True`:  
                    - Search **left half** for earlier occurrences (`right = mid - 1`).  
                - If `find_first=False`:  
                    - Search **right half** for later occurrences (`left = mid + 1`).  
            - If `nums[mid] < target`:  
                - Search **right half** (`left = mid + 1`).  
            - If `nums[mid] > target`:  
                - Search **left half** (`right = mid - 1`).  

        2. **Return Result**  
        - Returns `position` (index of first/last occurrence or `-1` if not found).  

        ### **Step 4: Find First and Last Occurrences**
        1. **First Occurrence**  
        - Call `find_position(nums, target, find_first=True)`.  
        - Searches leftward after finding `target` to locate the earliest instance.  

        2. **Last Occurrence**  
        - Call `find_position(nums, target, find_first=False)`.  
        - Searches rightward after finding `target` to locate the latest instance.  

        ### **Step 5: Return Final Result**
        - Returns `[first, last]` (indices of first and last occurrences).  
        - If `target` is not found, both values are `-1`.

---

### **Walkthrough Example**
**Input**: `nums = [5, 7, 7, 8, 8, 10]`, `target = 8`  

1. **Find First Occurrence (`find_first=True`)**  
   - **Initial**: `left = 0`, `right = 5`  
   - **Midpoint 1**: `mid = 2` → `nums[2] = 7` < `8` → search right (`left = 3`).  
   - **Midpoint 2**: `mid = 4` → `nums[4] = 8` == `8` → record `position = 4`, search left (`right = 3`).  
   - **Midpoint 3**: `mid = 3` → `nums[3] = 8` == `8` → update `position = 3`, search left (`right = 2`).  
   - **Loop Ends** → return `3`.  

2. **Find Last Occurrence (`find_first=False`)**  
   - **Initial**: `left = 0`, `right = 5`  
   - **Midpoint 1**: `mid = 2` → `nums[2] = 7` < `8` → search right (`left = 3`).  
   - **Midpoint 2**: `mid = 4` → `nums[4] = 8` == `8` → record `position = 4`, search right (`left = 5`).  
   - **Midpoint 3**: `mid = 5` → `nums[5] = 10` > `8` → search left (`right = 4`).  
   - **Loop Ends** → return `4`.  

3. **Final Result**: `[3, 4]`  

---

R - Review: 
    - **Time Complexity**: O(log n) for both searches (optimal for sorted arrays).  
    - **Space Complexity**: O(1) (no extra space used beyond variables).  
    - **Edge Cases Handled**: Empty array, single-element array, all elements identical.  
'''

def search_range(nums, target):
    """
    Finds the starting and ending positions of a target value in a sorted array.
    Uses binary search to achieve O(log n) runtime complexity.
    
    Args:
        nums: List of integers sorted in non-decreasing order
        target: Integer value to search for in the array
        
    Returns:
        A list containing [first_index, last_index] of target, 
        or [-1, -1] if target is not found
    """
    
    def find_position(nums, target, find_first):
        """
        Helper function to find either the first or last occurrence of target.
        
        Args:
            nums: The sorted array to search
            target: The value to find
            find_first: Boolean flag (True to find first occurrence, False for last)
            
        Returns:
            Index of the first/last occurrence, or -1 if not found
        """
        left, right = 0, len(nums) - 1  # Initialize search boundaries
        position = -1  # Default return value if target not found
        
        while left <= right:
            mid = left + (right - left) // 2  # Calculate middle index (prevents overflow)
            
            if nums[mid] == target:
                position = mid  # Store current position
                if find_first:
                    # For first occurrence, search left half to find earlier instances
                    right = mid - 1
                else:
                    # For last occurrence, search right half to find later instances
                    left = mid + 1
            elif nums[mid] < target:
                # Target must be in right half
                left = mid + 1
            else:
                # Target must be in left half
                right = mid - 1
                
        return position
    
    # Handle edge case of empty input array immediately
    if not nums:
        return [-1, -1]
    
    # Find first and last occurrences using helper function
    first = find_position(nums, target, True)  # Find first occurrence
    last = find_position(nums, target, False)   # Find last occurrence
    
    return [first, last]

#Standard Test Cases
# Test Case 1: Target exists with multiple occurrences
print(search_range([5,7,7,8,8,10], 8))   # Output: [3, 4]

# Test Case 2: Target doesn't exist in array
print(search_range([5,7,7,8,8,10], 6))   # Output: [-1, -1]

# Test Case 3: Empty array
print(search_range([], 0))                # Output: [-1, -1]

# Edge Case Test Cases
# Test Case 4: Target at beginning of array
print(search_range([2,2,3,4,5], 2))      # Output: [0, 1]

# Test Case 5: Target at end of array
print(search_range([1,2,3,4,5,5], 5))    # Output: [4, 5]

# Test Case 6: Single element array (target exists)
print(search_range([7], 7))               # Output: [0, 0]

# Test Case 7: Single element array (target missing)
print(search_range([3], 5))               # Output: [-1, -1]

# Special Case Test Cases
# Test Case 8: All elements are target
print(search_range([4,4,4,4,4], 4))      # Output: [0, 4]

# Test Case 9: Target appears once
print(search_range([1,3,5,7,9], 5))      # Output: [2, 2]

# Test Case 10: Large array
large_array = [i for i in range(100000)] + [99999]
print(search_range(large_array, 99999))   # Output: [99999, 100000]

# Verification Test Cases
# Test Case 11: Negative numbers
print(search_range([-5,-3,-3,0,1], -3))  # Output: [1, 2]

# Test Case 12: Mixed positive/negative
print(search_range([-2,0,0,1,2], 0))     # Output: [1, 2]

# Test Case 13: Floating point numbers
print(search_range([1.1,2.2,2.2,3.3], 2.2))  # Output: [1, 2]

'''
### Key Comments Explained:

1. **Main Function Docstring**:
   - Explains the overall purpose and behavior
   - Documents parameters and return value
   - Notes the time complexity

2. **Helper Function Docstring**:
   - Explains the specialized binary search behavior
   - Documents the `find_first` flag purpose
   - Clarifies return value meaning

3. **Algorithm Comments**:
   - Explains boundary initialization
   - Documents the mid-point calculation
   - Clarifies the three search cases:
     - When target is found
     - When target is in right half
     - When target is in left half

4. **Edge Case Handling**:
   - Explicitly notes the empty array check

5. **Function Calls**:
   - Comments explain what each helper call accomplishes

### Why This Matters:
1. **Maintainability**: Future developers can understand the logic quickly
2. **Debugging**: Clear comments help identify where issues might occur
3. **Knowledge Transfer**: Explains the binary search modifications
4. **Best Practices**: Demonstrates proper Python documentation standards
'''
