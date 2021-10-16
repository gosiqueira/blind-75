"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time. 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 
Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    """
    Time: O(n)
    Space: O(n)
    """
    if not nums:
        return 0
    
    nums = set(nums)
    longest = 1
    
    for num in nums:
        if num - 1 not in nums:
            curr = 1
            next_num = num + 1
            while next_num in nums:
                curr += 1
                next_num += 1
            longest = max(longest, curr)

    return longest


if __name__ == '__main__':
    # Test 1
    nums = [100, 4, 200, 1, 3, 2]
    print(longestConsecutive(nums))

    # Test 2
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longestConsecutive(nums))
