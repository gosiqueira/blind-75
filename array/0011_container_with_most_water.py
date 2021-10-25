"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
Notice that you may not slant the container. 

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1

Example 3:

Input: height = [4,3,2,1,4]
Output: 16

Example 4:

Input: height = [1,2,1]
Output: 2
 
Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from typing import List


def maxArea(height: List[int]) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        h = min(height[left], height[right])
        max_area = max(max_area, (right - left) * h)
        
        if height[left] <= h and left < right:
            left += 1
        elif height[right] <= h and left < right:
            right -= 1
            
    return max_area


if __name__ == '__main__':
    # Test 1
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))

    # Test 2
    height = [1,1]
    print(maxArea(height))

    # Test 3
    height = [4,3,2,1,4]
    print(maxArea(height))

    # Test 4
    height = [1,2,1]
    print(maxArea(height))
