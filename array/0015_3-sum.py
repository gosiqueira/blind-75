"""
Given an integer array nums, return all the triplets [nums[i], nums[j],
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []
 
Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    """
    Time: O(n^2)
    Space: O(1)
    """
    response = []
    nums.sort()

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                 r -= 1
            else:
                response.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    
    return response


if __name__ == "__main__":
    # Test 1
    print(threeSum([-1, 0, 1, 2, -1, -4]))

    # Test 2
    print(threeSum([]))

    # Test 3
    print(threeSum([0]))