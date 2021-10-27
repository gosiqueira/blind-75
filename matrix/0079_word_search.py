"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once. 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    Time: O(m*n^(l-1))
    Space: O(m*n)
    """
    visited = set()
    
    def dfs(idx, row, col):
        if not (0 <= row < len(board) and 0 <= col < len(board[0])) or (row, col) in visited or board[row][col] != word[idx]:
            return False

        if idx == len(word) - 1: return True

        visited.add((row, col))

        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dx, dy = x + row, y + col
            if dfs(idx + 1, dx, dy):
                return True

        visited.remove((row, col))

        return False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(0, i, j):
                return True

    return False


if __name__ == '__main__':
    # Test 1
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = 'ABCCED'
    print(exist(board, word))

    # Test 2
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = 'SEE'
    print(exist(board, word))

    # Test 3
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = 'ABCB'
    print(exist(board, word))
