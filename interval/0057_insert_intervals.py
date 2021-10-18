"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end
of the ith interval and intervals is sorted in ascending order by start_i. You are also given an interval newInterval = [start, end]
that represents the start and end of another interval.
Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and intervals still does not have
any overlapping intervals (merge overlapping intervals if necessary).
Return intervals after the insertion. 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Example 3:

Input: intervals = [], newInterval = [5,7]
Output: [[5,7]]

Example 4:

Input: intervals = [[1,5]], newInterval = [2,3]
Output: [[1,5]]

Example 5:

Input: intervals = [[1,5]], newInterval = [2,7]
Output: [[1,7]]

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= start_i <= end_i <= 105
intervals is sorted by start_i in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List


def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    """
    Time: O(n)
    Space: O(n)
    """
    result = []
        
    i = 0
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    if i < len(intervals):
        new_interval[0] = min(intervals[i][0], new_interval[0])
        
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[1] = max(intervals[i][1], new_interval[1])
        i += 1
        
    result.append(new_interval)
    
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
        
    return result


if __name__ == '__main__':
    # Test 1
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print(insert_interval(intervals, new_interval))

    # Test 2
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    print(insert_interval(intervals, new_interval))

    # Test 3
    intervals = []
    new_interval = [5,7]
    print(insert_interval(intervals, new_interval))

    # Test 4
    intervals = [[1,5]]
    new_interval = [2,3]
    print(insert_interval(intervals, new_interval))

    # Test 5
    intervals = [[1,5]]
    new_interval = [2,7]
    print(insert_interval(intervals, new_interval))
