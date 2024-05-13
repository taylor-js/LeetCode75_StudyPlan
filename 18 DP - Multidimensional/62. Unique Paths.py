# https://leetcode.com/problems/unique-paths/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    s = Solution()
    updp1 = s.uniquePaths(3, 7)
    print(updp1)  # Output: 28
    updp2 = s.uniquePaths(3, 2)
    print(updp2)  # Output: 3
