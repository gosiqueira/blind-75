"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0

Example 4:

Input: coins = [1], amount = 1
Output: 1

Example 5:

Input: coins = [1], amount = 2
Output: 2

Constraints:

1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    """
    Time: O(n * amount)
    Space: O(amount)
    """
    dp = [float('inf') for _ in range(amount + 1)]
    
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i-c] + 1)
            
    return -1 if dp[-1] == float('inf') else dp[-1]


if __name__ == '__main__':
    # Test 1
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))

    # Test 2
    coins = [2]
    amount = 3
    print(coinChange(coins, amount))

    # Test 3
    coins = [1]
    amount = 0
    print(coinChange(coins, amount))

    # Test 4
    coins = [1]
    amount = 1
    print(coinChange(coins, amount))

    # Test 5
    coins = [1]
    amount = 2
    print(coinChange(coins, amount))
