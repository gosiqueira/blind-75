"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Example 4:

Input: s = "([)]"
Output: false

Example 5:

Input: s = "{[]}"
Output: true 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

def isValid(s: str) -> bool:
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            if i == ')' and stack[-1] != '(':
                return False
            if i == ']' and stack[-1] != '[':
                return False
            if i == '}' and stack[-1] != '{':
                return False
            stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    # Test 1
    s = '()'
    print(isValid(s))

    # Test 2
    s = '()[]{}'
    print(isValid(s))

    # Test 3
    s = '(]'
    print(isValid(s))

    # Test 4
    s = '([)]'
    print(isValid(s))

    # Test 5
    s = '{[]}'
    print(isValid(s))