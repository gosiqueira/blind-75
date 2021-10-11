"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome. 

Constraints:

1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""

def isPalindrome(s: str) -> bool:
    letters = [char.lower() for char in s if char.isalnum()]
    
    return letters == letters[::-1]


def isPalindromeWithoutReverse(s: str) -> bool:
    left, right = 0, len(s) - 1
        
    while left < right:
        if not s[left].isalnum() and left < right:
            left += 1
            continue
            
        if not s[right].isalnum():
            right -= 1
            continue
            
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True


if __name__ == '__main__':
    # Test 1
    s = 'A man, a plan, a canal: Panama'
    print(isPalindrome(s))
    print(isPalindromeWithoutReverse(s))

    # Test 2
    s = 'race a car'
    print(isPalindrome(s))
    print(isPalindromeWithoutReverse(s))
