"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The answer is guaranteed to fit in a 32-bit integer. 

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
"""

from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    """
    Time: O(n * target)
    Space: O(target)
    """
    dp = [0 for _ in range(target + 1)]
    
    dp[0] = 1
    
    for i in range(target):
        for num in nums:
            if i + num <= target:
                dp[i + num] += dp[i]
                
    return dp[-1]


if __name__ == '__main__':
    # Test 1
    nums = [1, 2, 3]
    target = 4
    print(combinationSum4(nums, target))

    # Test 2
    nums = [9]
    target = 3
    print(combinationSum4(nums, target))
