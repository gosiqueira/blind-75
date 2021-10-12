"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step 

Constraints:

1 <= n <= 45
"""

def climbStairs(n: int) -> int:
    dp = [0 for _ in range(n + 1)]
    
    dp[0] = 1
    
    for i in range(1, n + 1):
        dp[i] = max(dp[i], dp[i-1] + dp[i-2])
        
    return dp[n]


if __name__ == "__main__":
    # Test 1
    n = 2
    print(climbStairs(n))

    # Test 2
    n = 3
    print(climbStairs(n))
