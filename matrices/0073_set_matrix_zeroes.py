"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
You must do it in place.

Example 1:

Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Time: O(n^2)
    Space: O(1)
    """
    row = False
    col = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i == 0:
                    row = True
                if j == 0:
                    col = True
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
    if row:
        for i in range(len(matrix[0])):
            matrix[0][i] = 0
    if col:
        for i in range(len(matrix)):
            matrix[i][0] = 0


if __name__ == "__main__":
    # Test 1
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    setZeroes(matrix)
    print(matrix)

    # Test 2
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    setZeroes(matrix)
    print(matrix)
