"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping. 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 
Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""

from typing import List


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    """
    Time: O(nlogn)
    Space: O(1)
    """
    intervals.sort(key = lambda x: x[0])
    
    start = intervals[-1][0]
    ans = 0
    for i in range(len(intervals) - 2, -1, -1):
        if intervals[i][1] > start:
            ans += 1
        else:
            start = intervals[i][0]
    
    return ans


if __name__ == '__main__':
    # Test 1
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    print(eraseOverlapIntervals(intervals))

    # Test 2
    intervals = [[1,2],[1,2],[1,2]]
    print(eraseOverlapIntervals(intervals))

    # Test 3
    intervals = [[1,2],[2,3]]
    print(eraseOverlapIntervals(intervals))
