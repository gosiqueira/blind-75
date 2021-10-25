"""
Given a string s, return the number of palindromic substrings in it.
A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa". 

Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""

def countSubstrings(s: str) -> int:
    """
    Time: O(n^2)
    Space: O(1)
    """
    n = len(s)
    res = len(s)
    for i in range(n):
        mid = i
        left = i - 1
        while mid < n and left >= 0 and s[mid] == s[left]:
            left -= 1
            mid  += 1
            res += 1
        
        left  = i - 1
        right = i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            left  -= 1
            right += 1
            res += 1
        
    return res


if __name__ == '__main__':
    # Test 1
    s = 'abc'
    print(countSubstrings(s))

    # Test 2
    s = 'aaa'
    print(countSubstrings(s))
