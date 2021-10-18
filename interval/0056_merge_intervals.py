"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input. 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Time: O(nlogn)
    Space: O(n)
    """
    merged = []
    
    for interval in sorted(intervals):
        if not merged or interval[0] > merged[-1][1]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged


if __name__ == '__main__':
    # Test 1
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge(intervals))

    # Test 2
    intervals = [[1,4],[4,5]]
    print(merge(intervals))
