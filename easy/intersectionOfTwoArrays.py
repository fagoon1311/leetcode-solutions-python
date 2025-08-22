# Leetcode 349 Intersection of Two Arrays --> https://leetcode.com/problems/intersection-of-two-arrays/description/

# Problem Statement ---> Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Approach --> Using HashMap
"""
--Create a hashmap to store the elements of the first array.
--Traverse the second array and check if the element is present in the hashmap.
--If present, add the element to the result list and remove it from the hashmap.
--Return the result list.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        res = []
        for num in nums1:
            seen[num] = 1

        for num in nums2:
            if num in seen and seen[num] == 1:
                res.append(num)
                seen[num] = 0

        return res


# ---- Test cases ----
if __name__ == "__main__":
    sol = Solution()

    # Test case 1: Common elements
    print(sol.intersection([1, 2, 2, 1], [2, 2]))  
    # Expected Output: [2]

    # Test case 2: Multiple common elements
    print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))  
    # Expected Output: [9, 4] (order doesn’t matter)

    # Test case 3: No intersection
    print(sol.intersection([1, 3, 5], [2, 4, 6]))  
    # Expected Output: []

    # Test case 4: One array empty
    print(sol.intersection([], [1, 2, 3]))  
    # Expected Output: []

    # Test case 5: Both arrays empty
    print(sol.intersection([], []))  
    # Expected Output: []

    # Test case 6: Same arrays
    print(sol.intersection([1, 2, 3], [1, 2, 3]))  
    # Expected Output: [1, 2, 3]



