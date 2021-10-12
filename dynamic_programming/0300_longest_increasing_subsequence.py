"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7]. 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1
 
Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104

Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""

from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    """
    Time: O(n^2)
    Space: O(n)
    """
    l = len(nums)
    if l < 2: return l
    
    max_len = 0
    dp = [1 for _ in range(l)]
    for i in range(l):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_len:
                max_len = dp[i]
            
    return max_len


if __name__ == '__main__':
    # Test 1
    nums = [10,9,2,5,3,7,101,18]
    print(lengthOfLIS(nums))

    # Test 2
    nums = [0,1,0,3,2,3]
    print(lengthOfLIS(nums))

    # Test 3
    nums = [7,7,7,7,7,7,7]
    print(lengthOfLIS(nums))
