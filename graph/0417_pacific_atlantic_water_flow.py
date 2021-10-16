"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches
the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c]
represents the height above sea level of the cell at coordinate (r, c).
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west
if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans. 

Example 1:

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:

Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]
 
Constraints:

m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

from collections import deque
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    """
    Time: O(rows * cols)
    Space: O(rows * cols)
    """

    if not heights: return None
    rows, cols = len(heights), len(heights[0])
    
    pacific = [[0 for _ in range(cols)] for _ in range(rows)]
    atlantic = [[0 for _ in range(cols)] for _ in range(rows)]
    
    start_nodes = [(r, cols - 1) for r in range(rows)]
    start_nodes.extend([(rows - 1, c) for c in range(cols)])
    
    queue = deque(start_nodes)
    while queue:
        x, y = queue.popleft()
        
        atlantic[x][y] = 1
        
        for i, j in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if 0 <= i < rows and 0 <= j < cols and heights[x][y] <= heights[i][j] and not atlantic[i][j]:
                queue.append((i, j))
                
                
    start_nodes = [(r, 0) for r in range(rows)]
    start_nodes.extend([(0, c) for c in range(cols)])
    
    queue = deque(start_nodes)
    while queue:
        x, y = queue.popleft()
        
        pacific[x][y] = 1
        
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1 ), (x, y + 1)]:
            if 0 <= i < rows and 0 <= j < cols and heights[x][y] <= heights[i][j] and not pacific[i][j]:
                queue.append((i, j))
                
    ans = []
    for r in range(rows):
        for c in range(cols):
            if atlantic[r][c] and pacific[r][c]:
                ans.append([r, c])
                
    return ans


if __name__ == '__main__':
    # Test 1
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(pacificAtlantic(heights))

    # Test 2
    heights = [[2,1],[1,2]]
    print(pacificAtlantic(heights))
