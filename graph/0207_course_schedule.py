"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

from collections import defaultdict
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Time: O(V + E)
    Space: O(V + E)
    """
    if numCourses == 0:
        return False
    
    graph = defaultdict(list)
    for u, v in prerequisites:
        graph[u].append(v)
    
    state = [0 for _ in range(numCourses)]
    
    def has_cycle(node: int) -> bool:
        if state[node] == -1:
            return True

        if state[node] == 1:
            return False
        
        state[node] = -1

        for neighbor in graph[node]:
            if has_cycle(neighbor):
                return True
            
        state[node] = 1
        
        return False

    for course in range(numCourses):
        if has_cycle(course):
            return False
    
    return True


if __name__ == '__main__':
    # Test 1
    numCourses = 2
    prerequisites = [[1,0]]
    print(canFinish(numCourses, prerequisites))

    # Test 2
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    print(canFinish(numCourses, prerequisites))
