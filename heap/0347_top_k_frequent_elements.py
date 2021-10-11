"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1] 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from collections import Counter
from heapq import heappush
from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Time: O(n log k)
    Space: O(n)
    """
    counter = Counter(nums)
    
    heap = []
    for key, val in counter.items():
        heappush(heap, (-val, key))
    
    return [val for _, val in heap[:k]]


if __name__ == '__main__':
    # Test 1
    nums = [1,1,1,2,2,3]
    k = 2
    print(topKFrequent(nums, k))

    # Test 2
    nums = [1]
    k = 1
    print(topKFrequent(nums, k))
