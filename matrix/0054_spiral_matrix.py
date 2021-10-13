"""
Given an m x n matrix, return all elements of the matrix in spiral order. 

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 
Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """
    Time: O(n^2)
    Space: O(1)
    """
    if not matrix:
        return []

    result = []
    row_start, row_end = 0, len(matrix) - 1
    col_start, col_end = 0, len(matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        for i in range(col_start, col_end + 1):
            result.append(matrix[row_start][i])
        row_start += 1

        for i in range(row_start, row_end + 1):
            result.append(matrix[i][col_end])
        col_end -= 1

        if row_start <= row_end:
            for i in range(col_end, col_start - 1, -1):
                result.append(matrix[row_end][i])
            row_end -= 1

        if col_start <= col_end:
            for i in range(row_end, row_start - 1, -1):
                result.append(matrix[i][col_start])
            col_start += 1

    return result


if __name__ == '__main__':
    # Test 1
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(spiralOrder(matrix))

    # Test 2
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(spiralOrder(matrix))