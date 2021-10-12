"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:

Input: nums = [1]
Output: 1

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 
Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

def maxSubArray(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    local_max = 0
    global_max = float('-inf')
    for n in nums:
        local_max = max(n, n + local_max)
        if local_max > global_max:
            global_max = local_max 
        
    return global_max


if __name__ == '__main__':
    # Test 1
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(nums))

    # Test 2
    nums = [1]
    print(maxSubArray(nums))

    # Test 3
    nums = [5,4,-1,7,8]
    print(maxSubArray(nums))
