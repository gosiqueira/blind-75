"""
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a" 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

def longestPalindrome(s: str) -> str:
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(s)
    res = s[0]
    for i in range(1, n):
        left = i - 1
        mid = i
        while s[left] == s[mid] and left >= 0 and mid < n:
            left -= 1
            mid += 1
        res = max(res, s[left + 1:mid], key=len)

        left = i - 1
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        res = max(res, s[left + 1:right], key=len)

    return res


if __name__ == '__main__':
    # Test 1
    s = "babad"
    print(longestPalindrome(s))

    # Test 2
    s = "cbbd"
    print(longestPalindrome(s))

    # Test 3
    s = "a"
    print(longestPalindrome(s))

    # Test 4
    s = "ac"
    print(longestPalindrome(s))
