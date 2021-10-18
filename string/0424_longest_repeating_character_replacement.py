"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations. 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

from collections import defaultdict


def characterReplacement(s: str, k: int) -> int:
    """
    Time: O(n)
    Space: O(1)
    """
    res, maxf = 1, 0
    counts = defaultdict(int)
    
    left = 0
    for right in range(len(s)):
        counts[s[right]] += 1
        maxf = max(maxf, counts[s[right]])
        
        if right - left + 1 - maxf > k:
            counts[s[left]] -= 1
            left += 1
        else:
            res = max(res, right - left + 1)
            
    return res


if __name__ == '__main__':
    # Test 1
    s = 'ABAB'
    k = 2
    print(characterReplacement(s, k))

    # Test 2
    s = 'AABABBA'
    k = 1
    print(characterReplacement(s, k))
