"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:

Input: a = 1, b = 2
Output: 3

Example 2:

Input: a = 2, b = 3
Output: 5
 
Constraints:

-1000 <= a, b <= 1000
"""

def getSum(a: int, b: int) -> int:
    """
    Time: O(1)
    Space: O(1)
    """
    mask = 0b11111111111111111111111111111111
    max_int = 0b01111111111111111111111111111111

    while b:
        a, b = (a ^ b) & mask, ((a & b) << 1) & mask

    return a if a <= max_int else ~(a ^ mask)


if __name__ == '__main__':
    # Test 1
    a = 1
    b = 2
    print(getSum(a, b))

    # Test 2
    a = 2
    b = 3
    print(getSum(a, b))
