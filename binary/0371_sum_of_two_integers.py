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
    maks = 1 << 32
    while b:
        a, b = (a ^ b) % maks, ((a & b) << 1) % maks

    return a if a < maks else ~(a % maks) + 1


if __name__ == '__main__':
    # Test 1
    a = 1
    b = 2
    print(getSum(a, b))

    # Test 2
    a = 2
    b = 3
    print(getSum(a, b))
