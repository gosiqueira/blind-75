"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
It is guaranteed that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array. 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 
Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


def maxProduct(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res = max(nums)
    cur_min, cur_max = 1, 1
    
    for n in nums:
        if n == 0:
            cur_min, cur_max = 1, 1
            
        cur_max, cur_min = max(cur_max * n, cur_min * n, n), min(cur_max * n, cur_min * n, n)
        
        res = max(res, cur_max)
        
    return res


if __name__ == '__main__':
    # Test 1
    nums = [2,3,-2,4]
    print(maxProduct(nums))

    # Test 2
    nums = [-2,0,-1]
    print(maxProduct(nums))
