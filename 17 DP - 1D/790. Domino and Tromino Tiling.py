# https://leetcode.com/problems/domino-and-tromino-tiling/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def numTilings(self, n: int) -> int:
        if n < 3:
            return n  # Direct return for n = 1 or n = 2
        if n == 3:
            return 5  # Direct return for n = 3
        
        m = int(10 ** 9 + 7)
        # Initialize dp for first four cases
        dp = [0] * (n + 1)
        dp[1], dp[2], dp[3] = 1, 2, 5
        
        # Fill dp array using the recurrence relation
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % m
        
        return dp[n]

if __name__ == "__main__":
    s = Solution()
    # Example 1
    nt1 = s.numTilings(3)
    print(nt1)  # Output: 5
    # Example 2
    nt2 = s.numTilings(1)
    print(nt1)  # Output: 1
