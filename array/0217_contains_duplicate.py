"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    visited = set()
    
    for n in nums:
        if n in visited:
            return True
        else:
            visited.add(n)
            
    return False


if __name__ == "__main__":
    # Test 1
    print(containsDuplicate([1,2,3,1]))

    # Test 2
    print(containsDuplicate([1,2,3,4]))

    # Test 3
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))