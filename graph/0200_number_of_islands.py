"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List


def numIslands(grid: List[List[str]]) -> int:
    """
    Time: O(m * n)
    Space: O(m * n)
    """
    rows = len(grid)
    cols = len(grid[0])
    
    visited = set()
    
    isles = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1' and (r, c) not in visited:
                dfs((r, c), grid, visited)
                isles += 1
                
    return isles


def dfs(root, grid, visited):
    delta_x = [-1, 1, 0, 0]
    delta_y = [0, 0, -1, 1]
    
    rows = len(grid)
    cols = len(grid[0])
    
    stack = [root]
    
    while stack:
        i, j = stack.pop()
        
        visited.add((i, j))
        
        for y, x in zip(delta_y, delta_x):
            if i + y >= 0 and i + y < rows and j + x >= 0 and j + x < cols and \
                grid[i + y][j + x] == '1' and (i + y, j + x) not in visited:
                stack.append((i + y, j + x))


if __name__ == '__main__':
    # Test 1
    grid = [
        ['1','1','1','1','0'],
        ['1','1','0','1','0'],
        ['1','1','0','0','0'],
        ['0','0','0','0','0']
    ]
    print(numIslands(grid))
    
    # Test 2
    grid = [
        ['1','1','0','0','0'],
        ['1','1','0','0','0'],
        ['0','0','1','0','0'],
        ['0','0','0','1','1']
    ]
    print(numIslands(grid))
