"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def isAnagram(s: str, t: str) -> bool:
    response = True
    if len(s) != len(t):
        response = False
    else:
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        for key in s_dict.keys():
            if key not in t_dict or s_dict[key] != t_dict[key]:
                response = False
        
    return response


if __name__ == '__main__':
    # Test 1
    s = 'anagram'
    t = 'nagaram'
    print(isAnagram(s, t))

    # Test 2
    s = 'rat'
    t = 'car'
    print(isAnagram(s, t))